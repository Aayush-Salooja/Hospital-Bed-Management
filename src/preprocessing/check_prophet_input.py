import pandas as pd

HOSPITAL = "Hospital A"
DEPARTMENT = "MED"

df = pd.read_csv(
    "./data/processed/hospital_daily_demand_complete.csv"
)

df = df[
    (df["hospital_name"] == HOSPITAL)
    &
    (df["department"] == DEPARTMENT)
]

df["date"] = pd.to_datetime(df["date"])

print("\n===== LAST 30 ROWS =====")
print(
    df[["date", "admissions"]]
    .tail(30)
)

print("\n===== NON-ZERO DAYS =====")
print(
    (df["admissions"] > 0).sum()
)

print("\n===== ZERO DAYS =====")
print(
    (df["admissions"] == 0).sum()
)