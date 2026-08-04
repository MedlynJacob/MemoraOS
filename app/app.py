import streamlit as st
from ui.applications import show_applications
from ui.dashboard import show_dashboard
from ui.resume_analyser import resume_analyser

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "💼 Applications",
        "📁 Documents"
    ]
)

if page == "🏠 Dashboard":
    show_dashboard()

# Resume Analyser
elif page == "📄 Resume Analyzer":
    resume_analyser()
elif page == "💼 Applications":
    show_applications()

elif page == "📁 Documents":
    st.header("Documents")