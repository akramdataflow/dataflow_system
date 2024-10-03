import streamlit as st


bill_page = st.Page(
    page = r'views\bill.py',
    default=True
)

expenses_page = st.Page(
    page = r'views\expenses.py',
    title='expenses',
)


search_page = st.Page(
    page = r'views\search.py',
    title='search',
)

viewer_page = st.Page(
    page = r'views\viewer.py',
    title='viewer',
)


pg = st.navigation(
    {
        'Bill':[bill_page],
        'Company accounts':[expenses_page],
        'edit':[viewer_page, search_page]
    }
)


pg.run()