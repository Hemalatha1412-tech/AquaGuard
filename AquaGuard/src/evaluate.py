import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("../data/processed/features.csv")

X = df.drop("water_availability", axis=1)
y = df["water_availability"]

model = joblib.load("../models/aquaguard_model.pkl")

pred = model.predict(X)

mae = mean_absolute_error(y, pred)
rmse = np.sqrt(mean_squared_error(y, pred))

print("MAE:", mae)
print("RMSE:", rmse)
