import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load('model.sav')

# Set up app title and description
st.title('Sales Prediction App')
st.write('Enter your advertising budgets below to predict sales.')

# User inputs
tv = st.number_input('TV Budget ($)', min_value=0.0, value=100.0, step=1.0)
radio = st.number_input('Radio Budget ($)', min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input('Newspaper Budget ($)', min_value=0.0, value=20.0, step=1.0)

# Predict button
if st.button('Predict Sales'):
    # Prepare the input features as a DataFrame to keep feature names
    input_data = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'Radio', 'Newspaper'])
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Sales: {prediction:.2f} M')
