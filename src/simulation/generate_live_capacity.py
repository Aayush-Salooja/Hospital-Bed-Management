import pandas as pd
import numpy as np

print("Loading hospital network...")

df = pd.read_csv(
    "./data/processed/hospital_network.csv"
)

np.random.seed(42)

# Simulate realistic occupancy

df["occupied_beds"] = [
    int(total * np.random.uniform(0.60, 0.95))
    for total in df["total_beds"]
]

df["available_beds"] = (
    df["total_beds"] -
    df["occupied_beds"]
)

df["occupied_icu_beds"] = [
    int(total * np.random.uniform(0.55, 0.98))
    for total in df["icu_beds"]
]

df["available_icu_beds"] = (
    df["icu_beds"] -
    df["occupied_icu_beds"]
)

df["bed_utilization_pct"] = (
    df["occupied_beds"]
    / df["total_beds"]
    * 100
).round(2)

df["icu_utilization_pct"] = (
    df["occupied_icu_beds"]
    / df["icu_beds"]
    * 100
).round(2)

print("\n===== LIVE CAPACITY =====")
print(
    df[
        [
            "hospital_name",
            "available_beds",
            "available_icu_beds",
            "bed_utilization_pct",
            "icu_utilization_pct"
        ]
    ]
)

df.to_csv(
    "./data/processed/live_capacity.csv",
    index=False
)

print(
    "\nSaved:"
)

print(
    "./data/processed/live_capacity.csv"
)