import pandas as pd

hospitals = [
    {
        "hospital_id": 1,
        "hospital_name": "Hospital A",
        "total_beds": 500,
        "icu_beds": 80,
        "doctors": 120,
        "nurses": 300,
        "latitude": 20.2961,
        "longitude": 85.8245,
        "specialties": "MED,SURG,CARD,NEURO"
    },
    {
        "hospital_id": 2,
        "hospital_name": "Hospital B",
        "total_beds": 350,
        "icu_beds": 50,
        "doctors": 80,
        "nurses": 180,
        "latitude": 20.3100,
        "longitude": 85.8100,
        "specialties": "MED,ORTHO,SURG"
    },
    {
        "hospital_id": 3,
        "hospital_name": "Hospital C",
        "total_beds": 600,
        "icu_beds": 100,
        "doctors": 150,
        "nurses": 350,
        "latitude": 20.2800,
        "longitude": 85.8500,
        "specialties": "MED,CARD,NEURO"
    },
    {
        "hospital_id": 4,
        "hospital_name": "Hospital D",
        "total_beds": 250,
        "icu_beds": 40,
        "doctors": 60,
        "nurses": 140,
        "latitude": 20.3300,
        "longitude": 85.7800,
        "specialties": "ORTHO,SURG"
    },
    {
        "hospital_id": 5,
        "hospital_name": "Hospital E",
        "total_beds": 450,
        "icu_beds": 70,
        "doctors": 110,
        "nurses": 250,
        "latitude": 20.2700,
        "longitude": 85.8700,
        "specialties": "MED,CARD,SURG"
    }
]

df = pd.DataFrame(hospitals)

df.to_csv(
    "./data/processed/hospital_network.csv",
    index=False
)

print(df)
print("\nSaved hospital_network.csv")