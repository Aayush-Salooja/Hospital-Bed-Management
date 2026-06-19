import pandas as pd
from tqdm import tqdm

print("Loading ICU stays...")

icu = pd.read_csv(
    "./data/raw/icu/icustays.csv",
    usecols=["intime", "outtime"]
)

icu["intime"] = pd.to_datetime(icu["intime"])
icu["outtime"] = pd.to_datetime(icu["outtime"])

start_date = icu["intime"].min().floor("D")
end_date = icu["outtime"].max().floor("D")

print("Date Range:")
print(start_date)
print(end_date)

all_dates = pd.date_range(
    start=start_date,
    end=end_date,
    freq="D"
)

occupancy = []

print("Calculating occupancy...")

for day in tqdm(all_dates):

    occupied = (
        (
            icu["intime"] <= day
        )
        &
        (
            icu["outtime"] >= day
        )
    ).sum()

    occupancy.append(
        [day, occupied]
    )

occupancy_df = pd.DataFrame(
    occupancy,
    columns=[
        "date",
        "icu_occupancy"
    ]
)

print("\nPreview:")
print(
    occupancy_df.head()
)

print("\nRows:")
print(
    len(occupancy_df)
)

print("\nMax Occupancy:")
print(
    occupancy_df["icu_occupancy"].max()
)

occupancy_df.to_csv(
    "./data/processed/true_icu_occupancy.csv",
    index=False
)

print(
    "\nSaved to:"
)
print(
    "./data/processed/true_icu_occupancy.csv"
)