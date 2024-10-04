import streamlit as st
import pandas as pd
from datetime import datetime
import os


st.set_page_config(layout='wide')

# Define the file path
data_path = r'..\dataflow_system\data\Amount data.csv'

def save_to_csv(data_path, name, Description, Amount):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Check if the file exists
    if not os.path.exists(data_path):
        # Create the CSV file with the appropriate headers if it doesn't exist
        headers = ['current_time', 'name', 'Description', 'Amount']
        pd.DataFrame(columns=headers).to_csv(data_path, index=False, encoding='utf-8-sig')

    # Create a new DataFrame with the new data
    df = pd.DataFrame([{
        'current_time': current_time,
        'name': name,
        'Description': Description,
        'Amount': Amount
    }])

    # Append to the CSV file without writing headers again
    df.to_csv(data_path, mode='a', header=False, index=False, encoding='utf-8-sig')

# Streamlit inputs
name = st.text_input('Name')
Description = st.text_area('Describe what the payment is for')
Amount = st.number_input('Amount', step=1000, min_value=0)

# Submit button
Submit = st.button('Submit')

# When Submit is clicked, save to CSV
if Submit:
    save_to_csv(data_path, name, Description, Amount)
    st.success('Order saved successfully!')
