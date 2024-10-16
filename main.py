import streamlit as st


bill_page = st.Page(
    page = 'views/bill.py',
    default=True
)

expenses_page = st.Page(
    page = 'views/expenses.py',
    title='expenses',
)


search_page = st.Page(
    page = 'views/search.py',
    title='search',
)

viewer_page = st.Page(
    page = 'views/viewer.py',
    title='viewer',
)

dashboard_page = st.Page(
    page = 'views/dashboard.py',
    title='Dashboard',    
)


pg = st.navigation(
    {
        'Bill':[bill_page],
        'Company accounts':[expenses_page],
        'edit':[viewer_page, search_page],
        'dashboard':[dashboard_page]
    }
)


pg.run()
