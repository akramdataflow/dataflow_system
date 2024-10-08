import streamlit as st
import sqlite3
from datetime import datetime

# Connect to the SQLite database
def get_db_connection():
    return sqlite3.connect(r"data\data.db")

# Get the last and first order number from the database
def get_order_numbers():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Get the first and last order number
    cur.execute("SELECT MIN(order_number), MAX(order_number) FROM customer_data")
    first_order, last_order = cur.fetchone()
    
    conn.close()
    return first_order, last_order

def get_invoice_data(order_number):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Fetch invoice data
    cur.execute("SELECT * FROM customer_data WHERE order_number = ?", (order_number,))
    invoice = cur.fetchone()
    
    conn.close()
    return invoice

def update_invoice_data(order_number, updated_data):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Update the invoice data
    cur.execute("""
        UPDATE customer_data
        SET customer_name = ?, domain = ?, price = ?, amount_received = ?, remaining_amount = ?, creation_time = ?
        WHERE order_number = ?
    """, (updated_data['customer_name'], updated_data['domain'], updated_data['price'], updated_data['amount_received'], updated_data['remaining_amount'], updated_data['creation_time'], order_number))
    
    conn.commit()
    conn.close()

def delete_invoice_data(order_number):
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Delete the invoice data
    cur.execute("DELETE FROM customer_data WHERE order_number = ?", (order_number,))
    
    conn.commit()
    conn.close()

# Streamlit UI
st.set_page_config(layout='wide')

first_order, last_order = get_order_numbers()
order_number = st.number_input('Order Number', min_value=first_order, max_value=last_order, step=1)

# Fetch invoice data from the database
invoice_data = get_invoice_data(order_number)

if invoice_data is not None:
    # Display current values in editable fields
    name = st.text_input('Customer Name', value=invoice_data[1])  # Index 1 corresponds to customer_name
    domain = st.text_input("Domain", value=invoice_data[2])  # Index 2 corresponds to domain
    price = st.number_input('Price', min_value=0.0, value=float(invoice_data[4]), step=0.01)  # Index 4 corresponds to price
    amount_received = st.number_input('Amount Received', min_value=0.0, value=float(invoice_data[9]), step=0.01)  # Index 9 corresponds to amount_received
    creation_time = invoice_data[5]  # Index 5 corresponds to creation_time
    discount = float(invoice_data[8])  # Index 8 corresponds to discount

    # Calculate remaining amount
    remaining_amount = price - amount_received - discount
    if amount_received >= (price - discount):
        remaining_amount = 0.0

    # Create a DataFrame to display
    data = {
        'Customer Name': [name],
        'Domain': [domain],
        'Price': [price],
        'Discount': [discount],
        'Amount Received': [amount_received],
        'Remaining Amount': [remaining_amount],
        'Creation Time': [creation_time]
    }

    st.table(data)

    # Submit button to save changes
    if st.button('Update Invoice'):
        updated_data = {
            'customer_name': name,
            'domain': domain,
            'price': price,
            'amount_received': amount_received,
            'remaining_amount': remaining_amount,
            'creation_time': creation_time  # Assuming creation time is not updated
        }
        update_invoice_data(order_number, updated_data)
        st.success('Invoice updated successfully!')
else:
    st.warning("No invoice found for the provided order number.")

if st.button('Delete Invoice'):
    delete_invoice_data(order_number)
    st.success('Invoice deleted successfully!')
