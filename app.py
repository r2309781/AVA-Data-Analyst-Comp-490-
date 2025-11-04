import streamlit as st
import pandas as pd

#st.title("App.py")

st.set_page_config(
    page_title="GURU • Sidebar Dashboard",
    page_icon="🧠",
    layout="wide",
)

pages = {
    "Navigation Bar": [
        st.Page("Dashboard.py", title="Dashboard Home"),
        st.Page("Sales_Analytics.py", title="Sales and Analytics"),
         st.Page("Trends_and_Analysis.py", title="Trends and Analysis"),
        st.Page("Inventory_Overview.py", title="Inventory Overview"),
         st.Page("Transactions.py", title="Transactions and Inventory"),
         st.Page("Agent.py", title="AI Insights"),
         st.Page("Reports.py", title="Reports"),
        st.Page("AIAgent.py", title="Another Agent"),
    ],
    "Resources": [
       # st.Page("learn.py", title="Learn about us"),
        #st.Page("trial.py", title="Try it out"),
    ],
}

pg = st.navigation(pages)
pg.run()


