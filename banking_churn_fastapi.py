from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class model_input(BaseModel):
    credit_score : int
    country : str
    gender : str
    age : int
    tenure : int 
    balance : float
    products_number : int
    credit_card : int
    active_member : int
    estimated_salary : float 

#Loading the saved model
churn_model = joblib.load("banking_churn_rfc.pkl")

@app.post('/churn_prediction')
def predict_churn(input_parameters : model_input):

    input_df = pd.DataFrame([input_parameters.model_dump()])

    prediction = churn_model.predict(input_df)

    if prediction[0] == 0:
        return "Customer has NOT left the bank"
    else:
        return "Customer HAS LEFT the bank"
    
   