import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("insurance_model.pkl")
model_columns = joblib.load("insurance_columns.pkl")

st.title("💰 Insurance Cost Prediction")

age = st.number_input("Age",18,100,30)
bmi = st.number_input("BMI",10.0,50.0,25.0)
children = st.number_input("Children",0,10,0)

sex = st.selectbox("Sex",["male","female"])
smoker = st.selectbox("Smoker",["yes","no"])
region = st.selectbox("Region",["southwest","southeast","northwest","northeast"])

input_dict = {
    "age":age,
    "bmi":bmi,
    "children":children
}

input_data = pd.DataFrame([input_dict])

for col in model_columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[model_columns]

if st.button("Predict Insurance Cost"):

    prediction = model.predict(input_data)

    usd_price = prediction[0]
    inr_price = usd_price * 91

    st.success(f"Estimated Insurance Cost: ₹{inr_price:,.2f}")