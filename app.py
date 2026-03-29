import streamlit as st
import pickle
import numpy as np
import requests
import os

# -------------------------------
# Download model from Drive
# -------------------------------
def download_model():
    file_id = "1JvwbHNVO5BCjfWGuqf5SVsr1XqKpPiCJ"
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    response = requests.get(url)

    with open("traffic_model.pkl", "wb") as f:
        f.write(response.content)

# Download only once
if not os.path.exists("traffic_model.pkl"):
    download_model()

# -------------------------------
# Load model
# -------------------------------
model = pickle.load(open("traffic_model.pkl", "rb"))

# -------------------------------
# App UI
# -------------------------------
st.title("🚦 Traffic Congestion Prediction App")

st.markdown("### Predict traffic level based on time and conditions")

# Inputs
hour = st.slider("Hour of Day (0–23)", 0, 23)

day_name = st.selectbox(
    "Day of Week",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

day_map = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2,
    "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}
day = day_map[day_name]

month = st.selectbox("Month", list(range(1, 13)))

temp = st.number_input("Temperature (Kelvin)", value=280.0)

clouds = st.slider("Cloud Cover (%)", 0, 100)

# Prediction
if st.button("Predict Traffic"):
    input_data = np.array([[hour, temp, day, month, clouds]])
    prediction = model.predict(input_data)

    st.success(f"🚗 Predicted Traffic Level: {prediction[0]}")

# Info
st.markdown("---")
st.info("💡 Traffic mainly depends on hour (peak times).")