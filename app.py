import streamlit as st
import numpy as np
import joblib

# Load trained artifacts
scaler = joblib.load("scaler.pkl")
kmeans = joblib.load("kmeans_model.pkl")

st.set_page_config(page_title="Customer Segmentation", layout="centered")

st.title("Customer Segmentation using K-Means")
st.write("Enter customer details to predict the segment")

# ---- INPUT FIELDS ----
# ⚠️ KEEP THIS ORDER EXACTLY SAME AS TRAINING ⚠️

age = st.number_input("Age", min_value=0, value=30)
annual_income = st.number_input("Annual Income", min_value=0, value=50000)
children = st.number_input("Number of Children", min_value=0, value=1)
family_size = st.number_input("Family Size", min_value=1, value=3)
spending_score = st.number_input("Spending Score", min_value=0, value=50)
monthly_spend = st.number_input("Monthly Spend", min_value=0, value=2000)
tenure = st.number_input("Customer Tenure (months)", min_value=0, value=12)

# Combine inputs
input_data = np.array([
    age,
    annual_income,
    children,
    family_size,
    spending_score,
    monthly_spend,
    tenure
]).reshape(1, -1)

# ---- PREDICTION ----
if st.button("Predict Customer Segment"):
    scaled_data = scaler.transform(input_data)
    cluster = kmeans.predict(scaled_data)[0]

    st.success(f"Customer belongs to **Segment {cluster}**")