# app.py
import streamlit as st
import pandas as pd
import pickle

# Set page style configurations
st.set_page_config(page_title="Calorie Requirement Predictor", page_icon="🥗", layout="centered")

st.title("🥗 Daily Calorie Requirement Predictor")
st.write("Enter your personal and physical metrics below to estimate your daily required caloric intake.")

# Load the trained pickle pipeline safely
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

try:
    model = load_model()
except FileNotFoundError:
    st.error("⚠️ 'model.pkl' not found. Please run your training script (`train.py`) first to generate the model file.")
    st.stop()

# Layout UI with Columns
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Years)", min_value=1, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
    weight = st.number_input("Weight (kg)", min_value=10, max_value=300, value=70)

with col2:
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    sleep_hours = st.slider("Daily Sleep (Hours)", min_value=2.0, max_value=14.0, value=7.0, step=0.5)
    water_intake = st.slider("Daily Water Intake (Liters)", min_value=0.5, max_value=10.0, value=2.5, step=0.1)
    goal = st.selectbox("Fitness Goal", ["Lose", "Maintain", "Gain"])
    diet_type = st.selectbox("Diet Type", ["Veg", "Non-Veg", "Vegan", "Jain"])

st.markdown("---")

# Prediction logic
if st.button("📊 Calculate Calories", type="primary"):
    # Structure input data identically to the original training DataFrame columns
    input_data = pd.DataFrame([{
        'Age': age,
        'Gender': gender,
        'Height_cm': height,
        'Weight_kg': weight,
        'Activity_Level': activity_level,
        'Sleep_Hours': sleep_hours,
        'Water_Intake_L': water_intake,
        'Goal': goal,
        'Diet_Type': diet_type
    }])
    
    # Generate prediction using our pipeline
    prediction = model.predict(input_data)[0]
    
    # Display result cleanly
    st.success(f"### Estimated Target: **{int(round(prediction))} kcal** / day")
    st.caption("Note: This is an automated machine-learning estimate based on your historical dataset parameters.")