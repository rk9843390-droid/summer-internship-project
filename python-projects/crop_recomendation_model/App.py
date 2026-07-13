import streamlit as st
import joblib

# Load model
model = joblib.load("Agro_model.pkl")

st.title("🌾 Crop Recommendation System")

with st.form("crop_form"):

    N = st.number_input("Nitrogen (N)", value=90)
    P = st.number_input("Phosphorus (P)", value=42)
    K = st.number_input("Potassium (K)", value=43)
    temperature = st.number_input("Temperature (°C)", value=20.8)
    humidity = st.number_input("Humidity (%)", value=82.0)
    ph = st.number_input("Soil pH", value=6.5)
    rainfall = st.number_input("Rainfall (mm)", value=202.9)

    submit = st.form_submit_button("Predict Crop")

if submit:
    sample = [[N, P, K, temperature, humidity, ph, rainfall]]
    prediction = model.predict(sample)
    st.success(f"Recommended Crop: {prediction[0]}")