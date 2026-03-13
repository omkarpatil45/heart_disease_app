import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.model_utils import predict_heart_disease

st.set_page_config(page_title="Heart Disease Detection App", layout="wide")

st.title("Heart Disease Prediction App")
st.markdown("Enter patient details below to predict the likelihood of heart disease.")

# Collect user input
age = st.number_input("Age", 18, 100, 40)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 400, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise-Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])

# Create input list
features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
            exang, oldpeak, slope, ca, thal]

if st.button("🔍 Predict"):
    prediction, probability = predict_heart_disease(features)
    if prediction == 1:
        st.error(f"⚠️ The model predicts **Heart Disease** with probability {probability:.2f}")
    else:
        st.success(f"✅ The model predicts **No Heart Disease** with probability {probability:.2f}")