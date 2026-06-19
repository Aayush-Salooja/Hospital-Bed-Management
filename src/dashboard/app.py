import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Hospital Bed & Resource Management System",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Hospital Bed & Resource Management System")

# --------------------------------------------------
# Load Data
# --------------------------------------------------

capacity = pd.read_csv(
    "./data/processed/live_capacity.csv"
)

staff = pd.read_csv(
    "./data/processed/staff_plan.csv"
)

shortage = pd.read_csv(
    "./data/processed/shortage_report.csv"
)

routing = pd.read_csv(
    "./data/processed/routing_options.csv"
)

forecast = pd.read_csv(
    "./outputs/hospitalA_MED_forecast.csv"
)

# --------------------------------------------------
# KPIs
# --------------------------------------------------

total_hospitals = len(capacity)

total_available_beds = capacity[
    "available_beds"
].sum()

total_available_icu = capacity[
    "available_icu_beds"
].sum()

avg_utilization = round(
    capacity["bed_utilization_pct"].mean(),
    2
)

st.subheader("System Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Hospitals",
    total_hospitals
)

c2.metric(
    "Available Beds",
    int(total_available_beds)
)

c3.metric(
    "Available ICU Beds",
    int(total_available_icu)
)

c4.metric(
    "Avg Utilization %",
    avg_utilization
)

st.divider()

# --------------------------------------------------
# Capacity
# --------------------------------------------------

st.header("🏥 Current Hospital Capacity")

st.dataframe(
    capacity,
    use_container_width=True
)

# --------------------------------------------------
# Capacity Chart
# --------------------------------------------------

fig = px.bar(
    capacity,
    x="hospital_name",
    y="available_beds",
    title="Available Beds by Hospital"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# Staff Planning
# --------------------------------------------------

st.header("👨‍⚕️ Staff Scheduling Recommendations")

st.dataframe(
    staff,
    use_container_width=True
)

# --------------------------------------------------
# Shortage Report
# --------------------------------------------------

st.header("⚠️ Predicted Shortages")

if (
    shortage["bed_shortage"].any()
    or
    shortage["icu_shortage"].any()
):
    st.error(
        "Potential shortages detected."
    )
else:
    st.success(
        "No shortages predicted."
    )

st.dataframe(
    shortage,
    use_container_width=True
)

# --------------------------------------------------
# Prophet Forecast
# --------------------------------------------------

st.header("📈 7-Day Admission Forecast")

forecast_view = forecast[
    ["ds", "yhat"]
].tail(7)

forecast_view.columns = [
    "Date",
    "Predicted Admissions"
]

st.dataframe(
    forecast_view,
    use_container_width=True
)

fig2 = px.line(
    forecast_view,
    x="Date",
    y="Predicted Admissions",
    markers=True,
    title="Predicted Admissions (Next 7 Days)"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------------------------
# ICU Forecast
# --------------------------------------------------

st.header("🫁 ICU Occupancy Forecast")

icu_forecast = pd.DataFrame({
    "Day": [
        "Day 1",
        "Day 2",
        "Day 3",
        "Day 4",
        "Day 5",
        "Day 6",
        "Day 7"
    ],
    "Predicted ICU Occupancy": [
        1.32,
        1.59,
        1.82,
        2.02,
        2.21,
        2.39,
        2.55
    ]
})

st.dataframe(
    icu_forecast,
    use_container_width=True
)

fig3 = px.line(
    icu_forecast,
    x="Day",
    y="Predicted ICU Occupancy",
    markers=True,
    title="ICU Occupancy Forecast"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# --------------------------------------------------
# Ambulance Routing
# --------------------------------------------------

st.header("🚑 Ambulance Routing")

st.dataframe(
    routing,
    use_container_width=True
)

best = routing.iloc[0]

st.success(
    f"""
Recommended Hospital: {best['hospital_name']}

Available Beds: {best['available_beds']}

Available ICU Beds: {best['available_icu_beds']}
"""
)

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    """
Built using:
MIMIC-IV + Prophet + LSTM + Streamlit

Features:
Admission Forecasting,
ICU Forecasting,
Staff Scheduling,
Shortage Prediction,
Ambulance Routing
"""
)