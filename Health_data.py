import streamlit as st
import plotly.express as px
import pandas as pd
#LOAD DATA
df = pd.read_csv("health_data_new.csv")
df.drop(columns="Unnamed: 0", inplace=True)
#TITLE
st.set_page_config(page_title="Health Data Dashboard", layout="wide")
st.title("🩺 Patient Risk Assessment Dashboard")
st.write("Smart Health Insights: Risk and Outcomes")
#SIDE BAR FILTERS
st.sidebar.header("Filter your Data")

city = st.sidebar.multiselect(
    "Select City(s)",
    options=df['City'].unique(),
    default=df['City'].unique()
)
diagnosis = st.sidebar.multiselect(
    "Select Diagnosis",
    options=df['Diagnosis'].unique(),
    default=df['Diagnosis'].unique()
)
#FILTERED DATA FRAME
filtered_df = df[
    (df['City'].isin(city)) &
    (df['Diagnosis'].isin(diagnosis)) 
]
if filtered_df.empty:
    st.warning("⚠️ No Data Selected. Please adjust your Selection")
    st.stop()
else:
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

#KEY METRICS
total_pts = len(filtered_df) #count number of patientes per city
avg_cholesterol = filtered_df['Cholesterol'].mean()
avg_Bp = filtered_df['Blood Pressure'].mean()
col1, col2, col3 = st.columns(3)
col1.metric("Total Patient Count", f"{total_pts:,}")
col2.metric("Average Blood Pressure(mmHg)", f"{avg_Bp:.2f}")
col3.metric("Average Cholesterol(mg/dl)", f"{avg_cholesterol:.2f}")
#TOP 5 HEALTHY DF
top_five_healthy_df = (
    filtered_df[filtered_df["Diagnosis"] == 'Healthy']
    .sort_values(by=["Age", 'Blood Pressure', 'Cholesterol'], ascending=[False, False, False])
    .head(5)
    )
if top_five_healthy_df.empty:
    st.warning("⚠️ No Healthy Patients Found in selection")
else:
    st.subheader("🔰 Top Five Healthiest Individuals")
    st.dataframe(top_five_healthy_df[['Patient ID', 'Age', 'Gender', 'City', 'Blood Pressure', 'Cholesterol']])

#VISUALIZATION
#BAR graph- Avg BP per City
avg_bp_by_city = filtered_df.groupby("City")['Blood Pressure'].mean().reset_index(name="Avg_BP")
fig_bar = px.bar(
    avg_bp_by_city,
    x="City",
    y="Avg_BP",
    title="1️⃣ Average Blood Pressure by City",
    text_auto=True
)
st.plotly_chart(fig_bar, use_container_width=True)
#PIE -- Patient count per diagnosis
patient_per_diagnosis = (
    filtered_df.groupby("Diagnosis")['Patient ID']
    .count()
    .reset_index(name="Patient_Count"))
fig_pt = px.pie(
    patient_per_diagnosis,
    names="Diagnosis",
    values="Patient_Count",
    title="2️⃣ Patients by Diagnosis"
)
st.plotly_chart(fig_pt, use_container_width=True)
#BOX plot --> BP by diagnosis
fig_box = px.box(
    filtered_df,
    x="Diagnosis",
    y="Blood Pressure",
    title="3️⃣ Average Blood Pressure By Diagnosis"
)
st.plotly_chart(fig_box, use_container_width=True)
#SCATTER Plot 
fig_scatter = px.scatter(
    filtered_df,
    x="Age", y="Cholesterol",
    color="Diagnosis",
    title="4️⃣ Cholesterol Variation by Age"
)
st.plotly_chart(fig_scatter, use_container_width=True)
#Line graph - BP with age
fig_line = px.line(
    filtered_df,
    x="Age",
    y="Blood Pressure",
    title="5️⃣ Blood Pressure Trend with Age",
    markers=True,
    color="Diagnosis"
)
st.plotly_chart(fig_line, use_container_width=True)
#DOWNLOAD CSV
csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download Filtered Data(CSV)",
    data=csv,
    mime="text/csv",
    file_name="Updated_health_record.csv"
)

