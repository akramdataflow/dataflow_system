import streamlit as st
import pandas as pd



# Define the file path for the customer data
customer_data_path = r'C:\Users\rf\Desktop\dataflow\dataflow_system\dataflow_system\data\coustumer data.csv'

# Load the customer data
def load_customer_data(data_path):
    try:
        df = pd.read_csv(data_path, encoding='utf-8-sig')
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Set up the Streamlit application
st.set_page_config(page_title='Customer Data', layout='wide')
st.title('Customer Data')

# Load the customer data
customer_data = load_customer_data(customer_data_path)

# Display the customer data if it was loaded successfully
if customer_data is not None and not customer_data.empty:
    st.dataframe(customer_data)
else:
    st.warning("No customer data found.")
