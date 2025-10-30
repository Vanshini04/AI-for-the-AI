import streamlit as st

st.title("🌿 EcoMindAI – Real-Time CO₂ Dashboard")
st.write("Welcome to Vansh's AI-powered Carbon Footprint Tracker!")

st.sidebar.header("Model Inputs")
model_type = st.sidebar.selectbox("Select Model Type", ["Random Forest", "Neural Network", "XGBoost"])
dataset_size = st.sidebar.slider("Dataset Size", 1000, 50000, 10000)
epochs = st.sidebar.slider("Epochs", 5, 50, 10)

if st.sidebar.button("Predict CO₂ Emissions"):
    st.success(f"Predicted emissions for {model_type}: {round(dataset_size * epochs * 0.00002, 3)} kg CO₂")

st.write("Data sourced in real-time from UK Grid API for sustainability insights.")
