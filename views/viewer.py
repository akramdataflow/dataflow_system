import streamlit as st
import pandas as pd

# Define the file paths for the data
customer_data_path = r'..\dataflow_system\data\coustumer data.csv'
income_data_path = r'..\dataflow_system\data\incume data.csv'
amount_data_path = r'..\dataflow_system\data\Amount data.csv'

# Load the data from CSV files
def load_data(data_path):
    try:
        df = pd.read_csv(data_path, encoding='utf-8-sig')
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Set up the Streamlit application
st.set_page_config(page_title='Data Management', layout='wide')
st.title('Data Management System')

# Load the data
customer_data = load_data(customer_data_path)
income_data = load_data(income_data_path)
amount_data = load_data(amount_data_path)

# Sidebar navigation
table_selection = st.sidebar.selectbox(
    'Select a table to view:',
    options=['Customer Data', 'Income Data', 'Amount Data']
)

# Display the selected table
if table_selection == 'Customer Data':
    if customer_data is not None and not customer_data.empty:
        st.subheader('Customer Data')
        st.dataframe(customer_data)
    else:
        st.warning("No customer data found.")

elif table_selection == 'Income Data':
    if income_data is not None and not income_data.empty:
        st.subheader('Income Data')
        st.dataframe(income_data)
    else:
        st.warning("No income data found.")

elif table_selection == 'Amount Data':
    if amount_data is not None and not amount_data.empty:
        st.subheader('Amount Data')
        st.dataframe(amount_data)
    else:
        st.warning("No amount data found.")
