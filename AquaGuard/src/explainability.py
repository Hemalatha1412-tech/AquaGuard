import shap
import pandas as pd
import joblib

df = pd.read_csv("../data/processed/features.csv")
X = df.drop("water_availability", axis=1)

model = joblib.load("../models/aquaguard_model.pkl")

explainer = shap.Explainer(model, X)
shap_values = explainer(X)

shap.plots.bar(shap_values)
