import pandas as pd
import math

print("Loading live capacity...")

df = pd.read_csv(
    "./data/processed/live_capacity.csv"
)

# -----------------------------
# Staffing Rules
# -----------------------------
#
# General Beds:
# 1 nurse per 5 patients
# 1 doctor per 20 patients
#
# ICU:
# 1 nurse per 2 ICU patients
# 1 doctor per 8 ICU patients
#
# -----------------------------

staff_plan = []

for _, row in df.iterrows():

    occupied_beds = row["occupied_beds"]
    occupied_icu = row["occupied_icu_beds"]

    nurses_general = math.ceil(
        occupied_beds / 5
    )

    doctors_general = math.ceil(
        occupied_beds / 20
    )

    nurses_icu = math.ceil(
        occupied_icu / 2
    )

    doctors_icu = math.ceil(
        occupied_icu / 8
    )

    total_nurses_needed = (
        nurses_general +
        nurses_icu
    )

    total_doctors_needed = (
        doctors_general +
        doctors_icu
    )

    nurse_gap = (
        row["nurses"] -
        total_nurses_needed
    )

    doctor_gap = (
        row["doctors"] -
        total_doctors_needed
    )

    staff_plan.append([
        row["hospital_name"],
        total_nurses_needed,
        total_doctors_needed,
        nurse_gap,
        doctor_gap
    ])

result = pd.DataFrame(
    staff_plan,
    columns=[
        "hospital_name",
        "nurses_needed",
        "doctors_needed",
        "nurse_surplus",
        "doctor_surplus"
    ]
)

print("\n===== STAFF PLAN =====")
print(result)

result.to_csv(
    "./data/processed/staff_plan.csv",
    index=False
)

print(
    "\nSaved:"
)
print(
    "./data/processed/staff_plan.csv"
)