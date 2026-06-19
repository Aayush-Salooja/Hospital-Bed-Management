import pandas as pd

print("Loading datasets...")

# Admissions data
admissions = pd.read_csv(
    "./data/raw/hosp/admissions.csv",
    usecols=["hadm_id", "admittime"]
)

# Department/service data
services = pd.read_csv(
    "./data/raw/hosp/services.csv",
    usecols=["hadm_id", "curr_service"]
)

print("Converting dates...")

admissions["admittime"] = pd.to_datetime(
    admissions["admittime"]
)

admissions["date"] = admissions["admittime"].dt.date

print("Merging datasets...")

df = admissions.merge(
    services,
    on="hadm_id",
    how="left"
)

print("Creating daily department admissions...")

department_daily = (
    df.groupby(
        ["date", "curr_service"]
    )
    .size()
    .reset_index(name="admissions")
)

department_daily.columns = [
    "date",
    "department",
    "admissions"
]

department_daily = department_daily.sort_values(
    ["date", "department"]
)

print("\nDataset Preview:")
print(department_daily.head(20))

print("\nTotal Rows:")
print(len(department_daily))

department_daily.to_csv(
    "./data/processed/department_daily_admissions.csv",
    index=False
)

print(
    "\nSaved to:\n"
    "./data/processed/department_daily_admissions.csv"
)