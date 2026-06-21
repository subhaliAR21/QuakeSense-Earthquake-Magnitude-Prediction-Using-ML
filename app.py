import streamlit as st
import joblib
import numpy as np

model = joblib.load("random_forest_earthquake_model.pkl")

st.title("QuakeSense — Earthquake Magnitude Predictor")
st.write("Enter seismic event features to predict earthquake magnitude.")

latitude = st.number_input("Latitude (deg)", value=35.0)
longitude = st.number_input("Longitude (deg)", value=-120.0)
depth = st.number_input("Depth (km)", value=10.0)
stations = st.number_input("Number of Stations", value=10)

if st.button("Predict Magnitude"):
    features = np.array([[latitude, longitude, depth, stations]])
    prediction = model.predict(features)
    st.success(f"Predicted Earthquake Magnitude: {prediction[0]:.2f}")