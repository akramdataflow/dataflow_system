import streamlit as st
from datetime import datetime

st.text_input('name')

st.text_area('Gel what will you pay the money')

st.number_input('Amount', min_value=0, step=1000)

