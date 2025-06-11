import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('sales_adv_pipeline.pkl')

# App title
st.title("📈 Sales Prediction App")
st.write("Enter your advertising spend to predict sales:")

# Input fields
tv = st.number_input("TV Advertising Budget (in thousands)", min_value=0.0, format="%.2f")
radio = st.number_input("Radio Advertising Budget (in thousands)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict Sales"):
    input_data = np.array([[tv, radio]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Sales: {prediction[0]:.2f} thousand units")