import pandas as pd

print("Loading live capacity...")

capacity = pd.read_csv(
    "./data/processed/live_capacity.csv"
)

# --------------------------------
# Forecast Inputs
# --------------------------------

# Prophet forecast for MED

forecast_admissions = 83

# LSTM ICU forecast

forecast_icu = 3

# --------------------------------
# Bed Demand Assumptions
# --------------------------------

BED_CONVERSION = 0.30
ICU_CONVERSION = 0.10

results = []

for _, row in capacity.iterrows():

    predicted_beds_needed = int(
        forecast_admissions *
        BED_CONVERSION
    )

    predicted_icu_needed = int(
        forecast_icu *
        ICU_CONVERSION
    )

    future_available_beds = (
        row["available_beds"]
        - predicted_beds_needed
    )

    future_available_icu = (
        row["available_icu_beds"]
        - predicted_icu_needed
    )

    bed_shortage = (
        future_available_beds < 0
    )

    icu_shortage = (
        future_available_icu < 0
    )

    results.append([
        row["hospital_name"],
        future_available_beds,
        future_available_icu,
        bed_shortage,
        icu_shortage
    ])

results_df = pd.DataFrame(
    results,
    columns=[
        "hospital_name",
        "future_available_beds",
        "future_available_icu",
        "bed_shortage",
        "icu_shortage"
    ]
)

print("\n===== SHORTAGE REPORT =====")
print(results_df)

results_df.to_csv(
    "./data/processed/shortage_report.csv",
    index=False
)

print("\nSaved:")
print("./data/processed/shortage_report.csv")