import pandas as pd
from prophet import Prophet
import joblib
import os

HOSPITAL = "Hospital A"
DEPARTMENT = "MED"

print("Loading realistic demand dataset...")

df = pd.read_csv(
    "./data/processed/realistic_hospital_demand.csv"
)

df = df[
    (df["hospital_name"] == HOSPITAL)
    &
    (df["department"] == DEPARTMENT)
].copy()

print("Rows found:", len(df))

df["date"] = pd.to_datetime(
    df["date"]
)

prophet_df = df[
    ["date", "admissions"]
]

prophet_df.columns = [
    "ds",
    "y"
]

print("\nAdmissions Statistics:")
print(
    prophet_df["y"].describe()
)

print("\nTraining Prophet...")

model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False
)

model.fit(prophet_df)

future = model.make_future_dataframe(
    periods=7
)

forecast = model.predict(
    future
)

forecast["yhat"] = (
    forecast["yhat"]
    .clip(lower=0)
)

os.makedirs(
    "./models",
    exist_ok=True
)

os.makedirs(
    "./outputs",
    exist_ok=True
)

joblib.dump(
    model,
    "./models/prophet_hospitalA_MED.pkl"
)

forecast.to_csv(
    "./outputs/hospitalA_MED_forecast.csv",
    index=False
)

print("\n===== NEXT 7 DAY FORECAST =====")

print(
    forecast[
        ["ds", "yhat"]
    ].tail(7)
)

print("\nSaved Model:")
print("./models/prophet_hospitalA_MED.pkl")