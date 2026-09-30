import streamlit as st

from analysis.uploaded_resume_analyzer import analyze_uploaded_documents
from analysis.analysis_parser import parse_analysis


def resume_analyser():
    st.header("📄 Resume Analyzer")

    st.caption(
        "Upload your resume and a job description to analyze your match."
    )

    resume_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        help="Upload your resume as a PDF."
    )

    job_description_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "txt"],
        help="Upload the job description as a PDF or TXT file."
    )

    company = st.text_input(
        "Company Name (optional)",
        placeholder="e.g. DoorDash"
    )

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    ):

        if resume_file is None:
            st.warning("Please upload your resume.")
            return

        if job_description_file is None:
            st.warning("Please upload a job description.")
            return

        try:
            with st.spinner(
                "Analyzing your resume...\n\n"
                "This may take a little while."
            ):
                analysis = analyze_uploaded_documents(
                    resume_file,
                    job_description_file,
                    company
                )

                result = parse_analysis(analysis)

            st.success("Analysis Complete!")

            st.divider()

            st.metric(
                "Resume Match",
                f"{result['score']}%"
            )

            st.divider()

            st.subheader("Strong Matches")
            st.write(result["strong_matches"])

            st.subheader("Missing Requirements")
            st.write(result["missing_requirements"])

            st.subheader("Experience Gaps")
            st.write(result["experience_gaps"])

            st.subheader("Relevant Projects")
            st.write(result["projects"])

            st.subheader("Resume Improvements")
            st.write(result["resume_improvements"])

            st.subheader("Interview Preparation")
            st.write(result["interview_preparation"])

            st.divider()

        except Exception as e:
            st.error(f"Analysis failed: {e}")