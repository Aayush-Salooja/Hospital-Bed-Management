import pandas as pd
import math

# --------------------------------
# Incoming Patient
# --------------------------------

PATIENT_LAT = 20.3000
PATIENT_LON = 85.8200

REQUIRED_DEPARTMENT = "MED"

# --------------------------------
# Load Capacity Dataset
# --------------------------------

df = pd.read_csv(
    "./data/processed/live_capacity.csv"
)

print("Loaded Hospitals:", len(df))

# --------------------------------
# Distance Function
# --------------------------------

def distance(lat1, lon1, lat2, lon2):

    return math.sqrt(
        (lat1 - lat2) ** 2 +
        (lon1 - lon2) ** 2
    )

# --------------------------------
# Routing Logic
# --------------------------------

candidates = []

for _, row in df.iterrows():

    specialties = str(row["specialties"])

    if REQUIRED_DEPARTMENT not in specialties:
        continue

    if row["available_beds"] <= 0:
        continue

    d = distance(
        PATIENT_LAT,
        PATIENT_LON,
        row["latitude"],
        row["longitude"]
    )

    candidates.append([
        row["hospital_name"],
        round(d, 4),
        row["available_beds"],
        row["available_icu_beds"],
        row["bed_utilization_pct"]
    ])

result = pd.DataFrame(
    candidates,
    columns=[
        "hospital_name",
        "distance",
        "available_beds",
        "available_icu_beds",
        "bed_utilization_pct"
    ]
)

result = result.sort_values(
    by="distance"
)

print("\n===== ROUTING OPTIONS =====")
print(result)

print("\n===== RECOMMENDED HOSPITAL =====")
print(result.iloc[0])

result.to_csv(
    "./data/processed/routing_options.csv",
    index=False
)

print("\nSaved:")
print("./data/processed/routing_options.csv")