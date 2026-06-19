# 🏥 Hospital Bed & Resource Management System

An AI-powered healthcare operations platform that forecasts patient admissions, predicts ICU occupancy, optimizes staff allocation, detects future shortages, and recommends ambulance routing using historical healthcare data and machine learning models.

---

## 🚀 Features

### 📈 Admission Forecasting
- Forecasts department-wise patient admissions for the next 7 days
- Built using Facebook Prophet
- Supports hospital-level demand prediction

### 🫁 ICU Occupancy Prediction
- Predicts ICU occupancy trends using LSTM neural networks
- Helps hospitals prepare for future demand

### 🏥 Hospital Capacity Monitoring
- Tracks:
  - Total beds
  - Available beds
  - ICU capacity
  - Utilization rates

### 👨‍⚕️ Staff Scheduling Recommendations
- Estimates doctor and nurse requirements
- Identifies staffing surpluses and shortages

### ⚠️ Shortage Prediction Engine
- Predicts future bed and ICU shortages
- Assists resource planning and allocation

### 🚑 Ambulance Routing
- Recommends the nearest suitable hospital
- Considers:
  - Bed availability
  - ICU availability
  - Hospital specialties

### 📊 Interactive Dashboard
- Built using Streamlit
- Real-time visualization of:
  - Capacity
  - Forecasts
  - Routing recommendations
  - Staffing insights

---

## 🧠 Machine Learning Models

| Task | Model |
|--------|--------|
| Admission Forecasting | Prophet |
| ICU Occupancy Forecasting | LSTM |
| Shortage Prediction | Forecast + Capacity Logic |
| Routing Recommendation | Distance + Capacity Scoring |

---

## 📂 Dataset

### Historical Data
- MIMIC-IV Clinical Database

### Synthetic Data
To simulate a realistic multi-hospital environment, synthetic operational datasets were generated for:
- Hospital networks
- Bed capacities
- Staff availability
- Hospital demand patterns

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Prophet
- TensorFlow / Keras
- Scikit-Learn
- Plotly
- Streamlit

---

## 📸 Dashboard Screenshots

### System Overview
![Overview](screenshots/dashboard_overview.png)

### Admission Forecast
![Forecast](screenshots/forecast.png)

### ICU Forecast
![ICU](screenshots/icu_forecast.png)

### Ambulance Routing
![Routing](screenshots/routing.png)

---

## 📁 Project Structure

```text
Hospital-Bed-Management
│
├── src
│   ├── dashboard
│   ├── models
│   ├── preprocessing
│   ├── routing
│   └── simulation
│
├── data
│   └── processed
│
├── models
├── outputs
├── screenshots
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run dashboard:

```bash
streamlit run src/dashboard/app.py
```

---

## 👨‍💻 Author

**Aayush Salooja**

GitHub: https://github.com/AayushSalooja/Hospital-Bed-Management
