import pandas as pd
import numpy as np

def generate_synthetic_global_data():
    np.random.seed(42)

    data = pd.DataFrame({
        "rainfall_mm": np.random.normal(800, 200, 500),
        "temperature": np.random.normal(25, 5, 500),
        "population_growth": np.random.uniform(0.5, 3, 500),
        "infrastructure_index": np.random.uniform(0.3, 0.9, 500),
        "groundwater_level": np.random.normal(50, 10, 500),
    })

    data["water_availability"] = (
        0.4 * data["rainfall_mm"]
        - 5 * data["temperature"]
        - 10 * data["population_growth"]
        + 50 * data["infrastructure_index"]
        + 2 * data["groundwater_level"]
    )

    data.to_csv("../data/raw/global_water_data.csv", index=False)

if __name__ == "__main__":
    generate_synthetic_global_data()
