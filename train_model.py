import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

df = pd.read_csv("real_emissions_data.csv")
le = LabelEncoder()
df["Model_Type_Encoded"] = le.fit_transform(df["Model_Type"])

X = df[["Model_Type_Encoded", "Dataset_Size", "Epochs"]]
y = df["CO2_Emissions_kg"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

joblib.dump(model, "co2_predictor_model.pkl")
joblib.dump(le, "label_encoder.pkl")
print("✅ Model saved.")
