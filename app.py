# Library imports
import uvicorn
from fastapi import FastAPI,Form
import numpy as np 
import pickle
import pandas as pd

# Create the app object
app = FastAPI()


@app.get('/favicon.ico', include_in_schema=False)


@app.get('/')
async def get_root():
    return {'message': 'Welcome to the diabetes predictions  API'}

# Expose the prediction functionality, make a prediction from the pass Form data and return the predicted Diabetes with the confidence
@app.post("/predict")
async def predict(Pregnancies:float = Form("0-100"), Glucose: float = Form("0-1000"), BloodPressure: float = Form("0-1000"), SkinThickness: float = Form("0-200"), Insulin: float = Form("0-1000"), BMI: float = Form("0-100"), DiabetesPedigreeFunction: float = Form("0.078-50.0"), Age: float = Form("21-98")):
    model = pickle.load(open("model.pk", "rb"))
    prediction = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]])
    probab = model.predict_proba([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]])


    if (prediction[0]>0.5):
        prediction = "Your chance of having diabetes is very high with {} probability based on this model (This is only a predictive model, please consult a certified doctor for any medical advice)".format(probab[0][1])
    else:
        prediction = "You have a low chance of diabetes with {} probability which is currently consider safe (This is only a predictive model, please consult a certified doctor for any medical advice)".format(probab[0][0])
    return {
        "prediction": prediction
    }

# Run the API with uvicorn
# Will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)