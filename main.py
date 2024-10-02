import streamlit as st


bill_page = st.Page(
    page = r'views\bill.py',
    default=True
)

expenses_page = st.Page(
    page = r'views\expenses.py',
    title='expenses',
)

pg = st.navigation(
    {
        'Bill':[bill_page],
        'Company accounts':[expenses_page]
    }
)


pg.run()