import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(layout='wide')

# Define the database path
data_path = "../dataflow_system/data/data.db"

# Connect to the SQLite database
conn = sqlite3.connect(data_path)
c = conn.cursor()

# Function to add data to the database
def add_data_amount(name, description, amount):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('''
        INSERT INTO Amount_data (current_time, name, description, amount)
        VALUES (?, ?, ?, ?)
    ''', (current_time, name, description, amount))
    conn.commit()

# Streamlit inputs
name = st.text_input('Name')
description = st.text_area('Describe what the payment is for')
amount = st.number_input('Amount', step=1000)

# Submit button
submit = st.button('Submit')

# When Submit is clicked, save to the database
if submit:
    add_data_amount(name, description, amount)
    st.success('Order saved successfully!')

# Close the connection when done
conn.close()
