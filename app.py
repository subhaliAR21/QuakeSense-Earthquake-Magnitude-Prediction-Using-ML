import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("random_forest_earthquake_model.pkl")

st.title("QuakeSense — Earthquake Magnitude Predictor")
st.write("Enter seismic event features to predict earthquake magnitude.")

latitude = st.number_input("Latitude", value=35.0)
longitude = st.number_input("Longitude", value=-120.0)
depth = st.number_input("Depth (km)", value=10.0)
year = st.number_input("Year", value=2024, min_value=1900, max_value=2100)
month = st.number_input("Month", value=1, min_value=1, max_value=12)
day = st.number_input("Day", value=1, min_value=1, max_value=31)
hour = st.number_input("Hour", value=0, min_value=0, max_value=23)

if st.button("Predict Magnitude"):
    features = pd.DataFrame([[latitude, longitude, depth, year, month, day, hour]],
                columns=['Latitude', 'Longitude', 'Depth', 'Year', 'Month', 'Day', 'Hour'])
    prediction = model.predict(features)
    st.success(f"Predicted Earthquake Magnitude: {prediction[0]:.2f}")