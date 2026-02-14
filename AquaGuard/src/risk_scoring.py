import pandas as pd
import joblib

model = joblib.load("../models/aquaguard_model.pkl")

df = pd.read_csv("../data/processed/features.csv")

pred = model.predict(df.drop("water_availability", axis=1))

df["risk_level"] = ["HIGH" if p < 200 else "LOW" for p in pred]

print(df[["risk_level"]].head())
