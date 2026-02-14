import pandas as pd

def engineer_features():
    df = pd.read_csv("../data/raw/global_water_data.csv")

    df["drought_index"] = df["temperature"] / df["rainfall_mm"]
    df["water_stress"] = df["population_growth"] / df["infrastructure_index"]

    df.to_csv("../data/processed/features.csv", index=False)

if __name__ == "__main__":
    engineer_features()
