
import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_data
def load_data():
    return pd.read_csv("customer_data/customers.csv")

def load_model():
    model_path = "churn_prediction/churn_model.pkl"
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

df = load_data()
model = load_model()

st.title("📊 Customer Churn Prediction & Retention Dashboard")

st.sidebar.header("Predict Churn for a New Customer")

age = st.sidebar.slider("Age", 18, 70, 30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
tenure = st.sidebar.slider("Tenure (months)", 1, 60, 12)
monthly_spend = st.sidebar.slider("Monthly Spend", 50, 500, 200)
support_tickets = st.sidebar.slider("Support Tickets", 0, 10, 2)
satisfaction = st.sidebar.slider("Satisfaction Score", 1, 10, 5)
policy_type = st.sidebar.selectbox("Policy Type", ["Life", "Health", "Vehicle", "Home"])
competitor = st.sidebar.selectbox("Has Competitor Policy", ["Yes", "No"])
region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])

if model:
    input_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Tenure": tenure,
        "MonthlySpend": monthly_spend,
        "SupportTickets": support_tickets,
        "SatisfactionScore": satisfaction,
        "PolicyType": policy_type,
        "HasCompetitorPolicy": competitor,
        "Region": region
    }])
    input_encoded = pd.get_dummies(input_df).reindex(columns=model.feature_names_in_, fill_value=0)
    prediction = model.predict(input_encoded)[0]
    st.sidebar.markdown("### Prediction: **{}**".format("Churn" if prediction else "Retain"))

st.subheader("Churn Overview")
col1, col2 = st.columns(2)
with col1:
    churn_rate = df['Churn'].mean() * 100
    st.metric("Churn Rate", f"{churn_rate:.2f}%")

with col2:
    st.metric("Total Customers", len(df))

st.subheader("Customer Segmentation by Policy Type")
st.bar_chart(df["PolicyType"].value_counts())

st.subheader("Average Monthly Spend by Region")
region_spend = df.groupby("Region")["MonthlySpend"].mean()
st.bar_chart(region_spend)

st.subheader("Retention Suggestions")
st.markdown("""
- 🟢 High satisfaction + long tenure → Offer loyalty perks.
- 🟡 Low satisfaction or high tickets → Personalized support follow-up.
- 🔴 Has competitor policy → Give incentives to switch.
""")
