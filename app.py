import streamlit as st
from PIL import Image 
import pickle

model = pickle.load(open('model.pk', 'rb'))

def run():
    img1 = Image.open("diabetes.jpg")
    img1 = img1.resize((156, 145))
    st.image(img1, use_column_width=False)
    st.title("Diabetes Prediction Using Machine Learning")


    ## Full Name
    fn = st.text_input("Full Name")

    ## Hospital  ID
    Hospital_id = st.text_input("Hospital ID")

    ## Number Pregnancies(1-100)
    preg_display = st.number_input("Number Pregnancies(0-100)", value=0)

    ## Glucose level
    glucose_level = st.number_input("Glucose Level(0-1000)", value=0)

    ## Blood Pressure
    blood_pre = st.number_input("Bood Pressure(0-1000)", value=0)

    ## Skin Thickness 
    skin_thickness = st.number_input("Skin Thickness(0-200)", value=0)

    ## Insulin
    insulin = st.number_input("Insulin(0-1000)", value=0)
    
    ## BMI
    bmi = st.number_input("BMI(0-100)", value=0)

    ## Diabetespedigreefunction 
    dia = st.number_input("Diabetespedigreefunction(0.078-50.0)", value=0)

    ## Age
    age = st.number_input("Age(21-98)", value=0)


    if st.button("Submit"):
        features = [[preg_display, glucose_level, blood_pre, skin_thickness, insulin, bmi, dia, age]]
        print(features)
        prediction = model.predict(features)
        lc =[str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 1:
            st.error(
                "Hello: " + fn + " || "
                "Hospital ID: " + Hospital_id + " || "
                "According to your input result, you have high chance of having diabetes" + "||"
                "This is just a predictive model, try to see a certified doctor for further consultation or medical advice"
            )
        else:
            st.success(
                "Hello: " + fn + " || "
                "Hospital ID: " + Hospital_id + " || "
                "According to your input result, you have low chance of having diabetes, which is consider safe" + "||"
                "This is just a predictive model, try to see a certified doctor for further consultation or medical advice"
            )

run()