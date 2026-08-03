import streamlit as st
from analysis.resume_job_analyser import analyze_resume
from analysis.analysis_parser import parse_analysis
from ui.applications import show_applications
import re

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
    st.header("Dashboard")

# Resume Analyser
elif page == "📄 Resume Analyzer":

    st.header("📄 Resume Analyzer")
    st.caption("Analyze how well your resume matches a job description.")
    company = st.text_input(
        "Company Name",
        placeholder="company"
    )

    if st.button("🚀 Analyze Resume", use_container_width=True):
        

        if company.strip() == "":
            st.warning("Please enter a company name.")

        with st.spinner("Analyzing resume...\n\nThis usually takes 30-60 seconds."):
            analysis = analyze_resume(company)
            result = parse_analysis(analysis)

        st.success("Analysis Complete!")
        st.divider()
        st.metric("Resume Match", f"{result['score']}%")
        st.divider()
        st.subheader("Analysis Details")
        st.subheader("Strong Matches")
        st.write(result['strong_matches'])
        st.subheader("Missing Requirements")
        st.write(result['missing_requirements'])
        st.subheader("Experience Gaps")
        st.write(result['experience_gaps'])
        st.subheader("Relevant Projects")
        st.write(result['projects'])
        st.subheader("Resume Improvements")
        st.write(result['resume_improvements'])
        st.subheader("Interview Preparation")
        st.write(result['interview_preparation'])
        st.divider()
        

elif page == "💼 Applications":
    show_applications()

elif page == "📁 Documents":
    st.header("Documents")