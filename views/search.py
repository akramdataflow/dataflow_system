import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(layout='wide')

# Define the file paths
data_path = r'..\dataflow_system\data\coustumer data.csv'


def get_last_order_number(data_path):
    df = pd.read_csv(data_path)
    return df['order number'].max()


def get_invoice_data(data_path, order_number):
    df = pd.read_csv(data_path)
    filtered_df = df[df['order number'] == order_number]
    
    if not filtered_df.empty:
        return filtered_df.iloc[0]
    else:
        return None


def update_invoice_data(data_path, order_number, updated_data):
    df = pd.read_csv(data_path)
    df.loc[df['order number'] == order_number, updated_data.keys()] = updated_data.values()
    df.to_csv(data_path, index=False, encoding='utf-8-sig')


# Streamlit inputs
order_number = st.number_input('Order number', min_value=1, max_value=get_last_order_number(data_path), step=1)

# Fetch invoice data from the CSV
invoice_data = get_invoice_data(data_path, order_number)

if invoice_data is not None:
    # Display current values in editable fields
    name = st.text_input('Customer Name', value=invoice_data['costumer name'])
    domain = st.text_input("Domain", value=invoice_data["Customer's field of work"])
    
    # Ensure parameters are floats
    price = st.number_input('Price', min_value=0.0, value=float(invoice_data['price']), step=0.01)
    amount_received = st.number_input('Amount Received', min_value=0.0, value=float(invoice_data['amount received']), step=0.01)
    creation_time = invoice_data['Creation time']
    
    # Retrieve discount from the invoice data
    discount = float(invoice_data['discount'])  # Get the discount value but do not display it

    # Calculate remaining amount
    remaining_amount = price - amount_received - discount

    # If the amount received covers the price after discount, set remaining amount to 0
    if amount_received >= (price - discount):
        remaining_amount = 0.0

    # Create a DataFrame to display
    data = {
        'Customer Name': [name],
        'Domain': [domain],
        'Price': [price],
        'Discount': [discount],  # Display the discount for reference
        'Amount Received': [amount_received],
        'Remaining Amount': [remaining_amount],
        'Creation Time': [creation_time]
    }

    df = pd.DataFrame(data)
    st.table(df)

    # Submit button to save changes
    if st.button('Update Invoice'):
        updated_data = {
            'costumer name': name,
            "Customer's field of work": domain,
            'price': price,
            'amount received': amount_received,
            'remaining amount': remaining_amount,
            'Creation time': creation_time  # Assuming creation time is not updated
        }
        update_invoice_data(data_path, order_number, updated_data)
        st.success('Invoice updated successfully!')
else:
    st.warning("No invoice found for the provided order number.")
