import streamlit as st
import numpy as np

# Linear Regression Coefficients
coefficients = [0.054510, 0.100946, 0.004340]
intercept = 4.7140

# Define the predictor class
class SalesPredictor:
    def __init__(self, coefficients, intercept):
        self.coefficients = np.array(coefficients)
        self.intercept = intercept

    def predict(self, inputs):
        return np.dot(inputs, self.coefficients) + self.intercept

# Initialize the predictor
predictor = SalesPredictor(coefficients, intercept)

# Page Title
st.title("Sales Prediction")
st.write("Enter the advertising budgets below to predict sales:")

# Input Fields
tv_budget = st.number_input("TV Advertising Budget", min_value=0.0, step=0.1)
radio_budget = st.number_input("Radio Advertising Budget", min_value=0.0, step=0.1)
newspaper_budget = st.number_input("Newspaper Advertising Budget", min_value=0.0, step=0.1)

# Prediction Button
if st.button("Predict Sales"):
    inputs = np.array([tv_budget, radio_budget, newspaper_budget])
    sales_prediction = predictor.predict(inputs)
    st.success(f"Predicted Sales: {sales_prediction:.2f}")
