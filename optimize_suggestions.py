import joblib, pandas as pd, numpy as np

model = joblib.load("co2_predictor_model.pkl")
le = joblib.load("label_encoder.pkl")

model_types = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Neural Network', 'XGBoost']
dataset_sizes = [1000, 5000, 10000, 20000, 50000]
epochs = [5, 10, 20, 30, 50]

combinations = [[m, s, e] for m in model_types for s in dataset_sizes for e in epochs]
opt_df = pd.DataFrame(combinations, columns=['Model_Type', 'Dataset_Size', 'Epochs'])
opt_df["Model_Type_Encoded"] = le.transform(opt_df["Model_Type"])

opt_df["Predicted_CO2_kg"] = model.predict(opt_df[["Model_Type_Encoded", "Dataset_Size", "Epochs"]])
best = opt_df.sort_values("Predicted_CO2_kg").head(5)
print("🌱 Greenest Configurations:\n", best)
