# 🌍 EcoMindAI — AI Carbon Footprint & Green Scheduler Dashboard

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-ff4b4b.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Sustainability](https://img.shields.io/badge/Goal-SDG%2013%20Climate%20Action-brightgreen)](https://sdgs.un.org/goals/goal13)

---

### 🧠 Overview

**EcoMindAI** is a sustainability-focused AI project that helps users measure, predict, and reduce **carbon emissions** generated from digital and AI-based activities.  
It combines **machine learning**, **live environmental data**, and an **interactive Streamlit dashboard** to promote *eco-conscious computing*.

---

### ⚙️ Features

🌿 **CO₂ Emission Tracker:**  
Uses the CodeCarbon library to measure emissions from simulated AI workloads.  

🔮 **AI Emission Predictor:**  
Trains a Random Forest model to estimate CO₂ based on dataset size, epochs, and training time.  

⚡ **Optimization Suggestions:**  
Identifies greenest model configurations and recommends eco-friendly alternatives.  

👩‍💻 **Dual User Modes:**  
- **Developer Mode:** For AI engineers to predict emissions of model training.  
- **Normal User Mode:** For everyday users to check emissions from digital activities.  

🌞 **Real-Time Green Scheduler:**  
Fetches live **carbon intensity data** via API and suggests the cleanest hours to run AI tasks.

---

### 🧩 Tech Stack

- **Python 3.10+**
- **Streamlit**
- **Scikit-learn**
- **Pandas / NumPy**
- **CodeCarbon**
- **Requests (Live API)**
- **Joblib**

---

### 📊 Architecture

```bash
EcoMindAI_Project/
│
├── app.py                         # Main Streamlit Dashboard
├── carbon_data_collection.py      # Emission dataset creation
├── train_model.py                 # Model training and evaluation
├── optimize_suggestions.py        # Green setup finder
├── realtime_api.py                # Live carbon intensity integration
├── requirements.txt               # Dependencies
└── README.md                      # Project description (this file)
