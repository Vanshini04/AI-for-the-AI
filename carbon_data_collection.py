from codecarbon import EmissionsTracker
import numpy as np, pandas as pd, random

tracker = EmissionsTracker(project_name="EcoMindAI", output_dir=".")
model_types = ['Logistic Regression', 'Decision Tree', 'Random Forest', 'Neural Network', 'XGBoost']
dataset_sizes = [1000, 5000, 10000, 20000, 50000]
epochs = [5, 10, 20, 30, 50]
records = []

for i in range(15):
    model = random.choice(model_types)
    size = random.choice(dataset_sizes)
    epoch = random.choice(epochs)
    tracker.start()
    x = np.random.rand(size, 50)
    for _ in range(epoch * 5):
        np.dot(x.T, x)
    emissions = tracker.stop()
    records.append([model, size, epoch, emissions])

df = pd.DataFrame(records, columns=['Model_Type', 'Dataset_Size', 'Epochs', 'CO2_Emissions_kg'])
df.to_csv("real_emissions_data.csv", index=False)
print("✅ Dataset saved as real_emissions_data.csv")
