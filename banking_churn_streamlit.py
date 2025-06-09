import pandas as pd
import joblib
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = joblib.load("banking_churn_rfc.pkl")
encoder = joblib.load("banking_churn_le.pkl")

credit_score = st.number_input("Credit Score (350 - 850)", min_value=350, max_value=850)
country = st.selectbox("Country", options=['France', 'Spain', 'Germany'])
gender = st.selectbox("Gender", options=['Male', 'Female'])
age = st.number_input("Age 18 - 92", min_value=18, max_value=92)
tenure = st.number_input("Tenure (0 - 10)", min_value=0, max_value=10)
balance = st.number_input("Bank (Balance 0 - 250898.09)", min_value=0.0, max_value=250898.09)
products_number = st.number_input("Number of products used (1 - 4)", min_value=1, max_value=4)
credit_card = st.number_input("Credit Cards [0: No, 1: Yes]", min_value=0, max_value=1)
active_member = st.number_input("Active Membership [0: No, 1: Yes]", min_value=0, max_value=1)
estimated_salary = st.number_input("Estimated Salary (11.58 - 199992.48)", min_value=11.58, max_value=199992.48)

input_data = {
    "credit_score": credit_score,
    "country": "country",
    "gender": "gender",
    "age": age,
    "tenure": tenure,
    "balance": balance,
    "products_number": products_number,
    "credit_card": credit_card,
    "active_member": active_member,
    "estimated_salary": estimated_salary
}

def predict_churn(input_data):
    input_df = pd.DataFrame([input_data])

    for col in ['country', 'gender']:
        if col in input_df.columns:
            input_df[col] = encoder.fit_transform(input_df[col])
    
    prediction = model.predict(input_df)
    return prediction

if st.button("Predict Churn"):
    prediction = predict_churn(input_data)

    if prediction == 0:
        st.info("Customer Status: Customer has NOT left the bank")
    else:
        st.info("Customer Status: Customer HAS LEFT the bank")

