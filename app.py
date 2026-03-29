import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load trained model
# -------------------------------
model = pickle.load(open('traffic_model.pkl', 'rb'))

# -------------------------------
# App Title
# -------------------------------
st.title("🚦 Traffic Congestion Prediction App")

st.markdown("### Predict traffic level based on time and conditions")

# -------------------------------
# User Inputs
# -------------------------------

# Hour input
hour = st.slider("Hour of Day (0–23)", 0, 23)

# Day input
day_name = st.selectbox(
    "Day of Week",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

# Convert day to numeric
day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}
day = day_map[day_name]

# Month input
month = st.selectbox("Month", list(range(1, 13)))

# Temperature input
temp = st.number_input("Temperature (Kelvin)", value=280.0)

# Cloud cover input
clouds = st.slider("Cloud Cover (%)", 0, 100)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Traffic"):

    # Arrange input in SAME order as training
    input_data = np.array([[hour, temp, day, month, clouds]])

    prediction = model.predict(input_data)

    st.success(f"🚗 Predicted Traffic Level: {prediction[0]}")

# -------------------------------
# Extra Info
# -------------------------------
st.markdown("---")
st.info("💡 Insight: Traffic is mainly influenced by hour of the day (peak hours).")