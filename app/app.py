import streamlit as st
from ui.applications import show_applications
from ui.resume_analyser import resume_analyser
from ui.dashboard import show_dashboard

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "💼 Applications"
    ]
)

if page == "🏠 Dashboard":
    show_dashboard()

# Resume Analyser
elif page == "📄 Resume Analyzer":
    resume_analyser()
elif page == "💼 Applications":
    show_applications()
