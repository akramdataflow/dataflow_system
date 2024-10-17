import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3
import warnings

# Set the color for numbers and text
number_color = '#50f296'

# Suppress warnings
warnings.filterwarnings('ignore')

# Configure the Streamlit page
st.set_page_config(page_title='udemy_courses_data', page_icon=':bar_chart:', layout='wide')

# Connect to SQLite database and load data
con = sqlite3.connect("../dataflow_system/data/data.db")
df = pd.read_sql_query('SELECT * FROM customer_data', con)
con.close()

# Calculate summary metrics
profit = df['price'].sum()  # Total profit
amount = df['amount_received'].sum()  # Total amount received
discount = df['discount'].sum()  # Total discount

# Create a container for scorecards
col1, col2, col3, col4 = st.columns(4)

# Display total amount received as a scorecard
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode="number",
    value=amount,
    title={"text": "Amount", 'font': {'color': number_color}},  # Title color and font
    number={'font': {'size': 150, 'color': number_color}}  # Number font size and color
))
col2.plotly_chart(fig, use_container_width=True)

# Display total profit as a scorecard
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode="number",
    value=profit,
    title={"text": "Sales", 'font': {'color': number_color}},  # Title color and font
    number={'font': {'size': 150, 'color': number_color}}  # Number font size and color
))
col1.plotly_chart(fig, use_container_width=True)

# Display remaining profit as a scorecard
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode="number",
    value=profit - amount - discount,  # Remaining profit calculation
    title={"text": "Remaining", 'font': {'color': number_color}},  # Title color and font
    number={'font': {'size': 150, 'color': number_color}}  # Number font size and color
))
col3.plotly_chart(fig, use_container_width=True)

# Display total number of customers as a scorecard
fig = go.Figure()
fig.add_trace(go.Indicator(
    mode="number",
    value=df['order_number'].count(),  # Count of customers
    title={"text": "Customers", 'font': {'color': number_color}},  # Title color and font
    number={'font': {'size': 150, 'color': number_color}}  # Number font size and color
))
col4.plotly_chart(fig, use_container_width=True)

# Create a bar chart for total price by domain
fig = px.bar(
    data_frame=df,
    x=df.groupby('domain')['price'].sum().sort_values(ascending=False).index,  # Domains on x-axis
    y=df.groupby('domain')['price'].sum().sort_values(ascending=False).values,  # Corresponding total prices
    text_auto='.2s'  # Auto-format text on bars
)

# Update layout for bar chart
fig.update_layout(
    title={
        'text': "Amount $",  # Title text
        'font': {
            'color': number_color,  # Title color
            'size': 24  # Title font size
        },
        'x': 0.5,  # Center title
        'xanchor': 'center'
    },
    xaxis_title={
        'text': "Domain",  # x-axis title text
        'font': {
            'size': 18,  # Font size for x-axis title
            'color': number_color  # Color for x-axis title
        }
    },
    yaxis_title={
        'text': "Count",  # y-axis title text
        'font': {
            'size': 18,  # Font size for y-axis title
            'color': number_color  # Color for y-axis title
        }
    },
    xaxis_tickfont=dict(size=25),  # Font size for x-axis tick labels
    yaxis_tickfont=dict(size=20),  # Font size for y-axis tick labels
)

# Display the bar chart
st.plotly_chart(fig, use_container_width=True)

# Create a histogram for count of amounts by domain
fig = px.histogram(
    data_frame=df,
    x = df['domain'].sort_values(ascending=False),  # Use 'domain' directly for x-axis
    title='Count Amount',  # Title text
    text_auto='.2s'  # Auto-format text on bars
)

# Update layout for histogram
fig.update_layout(
    title={
        'text': "Count Amount",  # Title text
        'font': {
            'color': number_color,  # Title color
            'size': 24  # Title font size
        },
        'x': 0.5,  # Center title
        'xanchor': 'center'
    },
    xaxis_title={
        'text': "Domain",  # x-axis title text
        'font': {
            'size': 18,  # Font size for x-axis title
            'color': number_color  # Color for x-axis title
        }
    },
    yaxis_title={
        'text': "Count",  # y-axis title text
        'font': {
            'size': 18,  # Font size for y-axis title
            'color': number_color  # Color for y-axis title
        }
    },
    xaxis_tickfont=dict(size=25),  # Font size for x-axis tick labels
    yaxis_tickfont=dict(size=20),  # Font size for y-axis tick labels
)

# Display the histogram
st.plotly_chart(fig, use_container_width=True)


remaining = df.groupby('customer_name')['remaining_amount'].sum().sort_values(ascending=False).head()

col1,col2 = st.columns([0.25,0.75])

with col1:
    with st.expander('Subject View Data'):
        # Convert Series to DataFrame
        remaining_df = remaining.reset_index()

        # Apply styling to the DataFrame
        styled_df = remaining_df.style.format({'remaining_amount': '${:,.2f}'}).background_gradient(cmap='Blues')

        # Display the styled DataFrame
        st.write(styled_df)

        # Convert to CSV
        csv_category = remaining_df.to_csv(index=False).encode('utf-8')
