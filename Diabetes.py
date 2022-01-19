from pydantic import BaseModel 

# class which describes Diabetes measurement 

class Diabete(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float 
    Age: float