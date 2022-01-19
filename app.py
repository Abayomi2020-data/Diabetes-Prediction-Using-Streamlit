# Library imports
from statistics import variance
import uvicorn
from fastapi import FastAPI
from Diabetes import Diabete
import numpy as np 
import pickle
import pandas as pd

# Create the app object

app = FastAPI()

pickle_in = open("model.pk", "rb")
classifier = pickle.load(pickle_in)

# Index route, opens automatically http://127.0.0.1:8000
@app.get("/")
def index():
    return {'message': 'Hello, World'}

# Route with a single parameter, returns the parameter within a message 
# Located at: http://127.0.0.1:800/AnyNameHere

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to diabetes web app': f'{name}'}

# Expose the prediction functionality, make a prediction from the pass JSON data and return the predicted Diabetes with the confidence
@app.post('/predict')
def predict_diabetes(data: Diabete):
    data = data.dict()
    Pregnancies = data["Pregnancies"]
    print(Pregnancies)
    Glucose = data["Glucose"]
    BloodPressure = data["BloodPressure"]
    SkinThickness = data["SkinThickness"]
    Insulin = data["Insulin"]
    BMI = data["BMI"]
    DiabetesPedigreeFunction = data["DiabetesPedigreeFunction"]
    Age = data["Age"]
#   print(classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFunction,Age]]))
    prediction = classifier.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFunction,Age]])
    if prediction[0]>(0.5):
        prediction = "Your chance of having diabetes is very high based on this model (This is only a predictive model, please consult a certified doctor for any medical advice)"
    else:
        prediction = "You have a low chance of diabetes which is currently consider safe (This is only a predictive model, please consult a certified doctor for any medical advice)"
    return {
        "prediction": prediction

    }


# Run the API with uvicorn
# Will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)