import pandas as pd
import numpy as np

print("Loading hospital network...")

hospitals = pd.read_csv(
    "./data/processed/hospital_network.csv"
)

# ---------------------------------
# Department Demand Weights
# ---------------------------------

DEPARTMENTS = {
    "MED": 1.8,
    "CMED": 1.6,
    "NMED": 1.5,
    "SURG": 1.3,
    "CSURG": 1.2,
    "NSURG": 1.2,
    "VSURG": 1.1,
    "ORTHO": 0.9,
    "GYN": 0.8,
    "OBS": 0.8,
    "ENT": 0.6
}

dates = pd.date_range(
    start="2021-01-01",
    end="2025-12-31",
    freq="D"
)

np.random.seed(42)

rows = []

print("Generating demand...")

for _, hospital in hospitals.iterrows():

    bed_factor = (
        hospital["total_beds"] / 250
    )

    for department, weight in DEPARTMENTS.items():

        base = (
            20
            * bed_factor
            * weight
        )

        for date in dates:

            weekly_effect = (
                1 +
                0.15 *
                np.sin(
                    2 * np.pi *
                    date.dayofweek / 7
                )
            )

            yearly_effect = (
                1 +
                0.10 *
                np.sin(
                    2 * np.pi *
                    date.dayofyear / 365
                )
            )

            noise = np.random.normal(
                1,
                0.10
            )

            admissions = int(
                base *
                weekly_effect *
                yearly_effect *
                noise
            )

            admissions = max(
                admissions,
                0
            )

            rows.append([
                date,
                hospital["hospital_name"],
                department,
                admissions
            ])

df = pd.DataFrame(
    rows,
    columns=[
        "date",
        "hospital_name",
        "department",
        "admissions"
    ]
)

print(df.head())

print("\nRows:")
print(len(df))

df.to_csv(
    "./data/processed/realistic_hospital_demand.csv",
    index=False
)

print(
    "\nSaved:"
)
print(
    "./data/processed/realistic_hospital_demand.csv"
)