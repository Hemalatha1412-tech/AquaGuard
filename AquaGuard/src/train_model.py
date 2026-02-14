import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("../data/processed/features.csv")

X = df.drop("water_availability", axis=1)
y = df["water_availability"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GradientBoostingRegressor()
model.fit(X_train, y_train)

joblib.dump(model, "../models/aquaguard_model.pkl")
print("Model trained")
