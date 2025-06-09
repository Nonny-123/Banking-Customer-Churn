🏦 Banking Customer Churn Prediction

This project predicts whether a customer will leave a bank (churn) using key banking and demographic features. The model is deployed using Streamlit for an interactive web interface and FastAPI for API integration. It's ideal for fintech companies interested in churn reduction and customer retention strategies.

🚀 Project Overview

Churn prediction helps banks and fintech institutions identify customers likely to leave, so proactive retention strategies can be implemented. Using machine learning (Random Forest Classifier), this project predicts churn based on features like credit score, age, balance, country, and more.

📂 Files in This Repository

banking_churn_rfc.pkl – Trained machine learning model (Random Forest)

bank_churn_notebook.ipynb – Jupyter Notebook with EDA, preprocessing, and model training

streamlit_app.py – Streamlit app for interactive predictions

main.py – FastAPI app for serving the model as an API

requirements.txt – Required Python libraries

🧠 Model Features

The model uses the following input features:

credit_score

country

gender

age

tenure

balance

products_number

credit_card (0: No, 1: Yes)

active_member (0: No, 1: Yes)

estimated_salary

Target: churn

1 = Customer has left the bank

0 = Customer has not left the bank

🛠️ How to Run the Project

1. Clone the Repo

git clone https://github.com/YourUsername/banking-churn-prediction.git
cd banking-churn-prediction

2. Create a Virtual Environment and Install Dependencies

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the Streamlit App

streamlit run streamlit_app.py

Visit: http://localhost:8501 in your browser.

4. Run the FastAPI Server

uvicorn main:app --reload

Visit the FastAPI docs at: http://127.0.0.1:8000/docs

📈 Sample Use Case

A user fills in values on the Streamlit interface, clicks Predict Churn, and instantly sees whether the customer is likely to stay or leave. The FastAPI endpoint /churn_prediction accepts JSON and returns the prediction — ideal for backend or mobile app integrations.

✅ Requirements

To install required libraries, run:

pip install -r requirements.txt

Main libraries used:

pandas

scikit-learn

joblib

streamlit

fastapi

uvicorn

pydantic

🔍 Future Improvements

Add model explainability using SHAP or LIME

Improve feature engineering (encode categorical features properly)

Dockerize the app for deployment

Add authentication to the API endpoints

✉️ Contact

Built by Okonji Chukwunonyelim Gabriel – Data Scientsist/ ML Engineer
nonnyokonji@gmail.com
