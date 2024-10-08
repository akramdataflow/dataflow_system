import streamlit as st
from datetime import datetime
import sqlite3
import os


# Configure the layout of the page
st.set_page_config(layout="wide")

# Define file paths
data = r"..\dataflow_system\data\data.db"

# Function to insert customer data into the SQLite database
def add_data(data_path, name, domain, description, price, creation_time, request_type, duration_of_completion, discount, amount_received, remaining_amount, phone_number):
    con = sqlite3.connect(data_path)
    cur = con.cursor()

    # New data as a tuple
    new_data = (name, domain, description, price, creation_time, request_type, duration_of_completion, discount, amount_received, remaining_amount, phone_number,)

    # Execute the insert query
    cur.execute(""" 
    INSERT INTO customer_data (customer_name,domain,description,price,creation_time,order_type,completion_time,discount,amount_received,remaining_amount,phone_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", new_data)

    # Commit the transaction and close the connection
    con.commit()
    con.close()

# Streamlit application layout
st.title('Customer Bill')

col1, col2 = st.columns(2)

with col1:
    name = st.text_input('Name')

with col2:
    domain = st.text_input('Domain')

phone_number = st.number_input('Phone Number', min_value=0)

description = st.text_area('Description')
request_type = st.text_area('Request Type')

duration_of_completion = st.date_input('Duration of Completion')

price = st.number_input('Price', min_value=0, step=1000)
discount = st.number_input('Discount', min_value=0, step=1)

# Correct label for the amount received
amount_received = st.number_input('Amount Received', min_value=0, step=100)

# Calculate remaining amount
remaining_amount = price - amount_received - discount  # Ensure remaining amount is not negative

# Current date and time
creation_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Add button to save the data
if st.button('Submit'):
    
        add_data(data, name, domain, description, price, creation_time, request_type, duration_of_completion, discount, amount_received, remaining_amount, phone_number)
        st.success(f"Data for {name} added successfully!")
