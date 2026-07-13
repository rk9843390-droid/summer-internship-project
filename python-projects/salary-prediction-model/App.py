import streamlit as st
import joblib

# -----------------------------
# Page Design
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #d4fc79, #96e6a1);
}

h1 {
    color: darkblue;
    text-align: center;
}

div.stButton > button {
    background-color: orange;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    width: 100%;
}

div.stButton > button:hover {
    background-color: green;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("salary_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("💰 Employee Salary Prediction")

st.write("Enter Employee Details")

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input("Age", 18, 60, 30)
experience = st.number_input("Years of Experience", 0, 40, 5)
city = st.selectbox("City Tier", [1, 2, 3])
performance = st.slider("Performance Score", 1, 10, 8)
skills = st.number_input("Number of Skills", 1, 20, 6)
remote = st.selectbox("Remote Work", [0, 1])

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Salary"):

    # Fixed values:
    # Education = Master
    # Job Role = ML Engineer
    x = [[
        age,
        experience,
        city,
        performance,
        skills,
        remote,
        0, 1, 0,      # Education
        0, 1, 0, 0, 0 # Job Role
    ]]

    prediction = model.predict(x)

    st.markdown(f"""
    <div style="
        background-color:#2E8B57;
        padding:20px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-size:28px;
        font-weight:bold;">
        💵 Predicted Salary <br><br>
        ${prediction[0]:,.2f}
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Developed using Streamlit")