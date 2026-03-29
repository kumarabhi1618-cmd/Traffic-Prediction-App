# 🚦 Traffic Congestion Prediction App

## 📌 Overview

This project is a machine learning-based web application that predicts traffic congestion levels (Low, Medium, High) based on time and environmental conditions.

The model is trained using historical traffic and weather data and deployed using Streamlit for real-time predictions.

---

## 🌐 Live Website

👉 **Try the app here:**
https://traffic-prediction-app-ntyjqjkrtweaoluzwwonn5.streamlit.app/

---

## 🚀 Features

* Predict traffic congestion level instantly
* User-friendly interactive web interface
* Optimized Random Forest model
* Lightweight and fast prediction system
* Deployed online using Streamlit Cloud

---

## 🧠 Machine Learning Workflow

1. Data preprocessing and cleaning
2. Feature engineering (time-based features)
3. Model training using Random Forest
4. Hyperparameter tuning using GridSearchCV
5. Feature importance analysis
6. Model optimization using top features
7. Deployment using Streamlit

---

## 📊 Key Insights

* **Hour of the day** is the most important factor affecting traffic
* Traffic peaks during morning and evening hours
* Weather conditions have comparatively low impact
* Weekdays show higher congestion than weekends

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
Traffic_Project/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/traffic-prediction-app.git
cd traffic-prediction-app
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run the App

```
streamlit run app.py
```

---

## 📈 Model Details

* Algorithm: Random Forest Classifier
* Hyperparameters:

  * n_estimators = 100
  * max_depth = None
  * min_samples_split = 5
  * min_samples_leaf = 1

---

## 🔍 Input Features

* Hour of the day
* Day of the week
* Month
* Temperature
* Cloud coverage

---

## 🎯 Output

* Traffic Level:

  * Low 🚗
  * Medium 🚗🚗
  * High 🚗🚗🚗

---

## 📚 References

* Dataset:
  Metro Interstate Traffic Volume Dataset
  https://archive.ics.uci.edu/ml/datasets/Metro+Interstate+Traffic+Volume

* Deployment Platform:
  Streamlit Community Cloud
  https://share.streamlit.io

* Machine Learning Library:
  Scikit-learn Documentation
  https://scikit-learn.org

---

## 💡 Future Improvements

* Add real-time traffic data integration
* Include map visualization
* Integrate weather APIs
* Improve accuracy using advanced models

---

## 🙌 Author

**Abhishek Kumar**

