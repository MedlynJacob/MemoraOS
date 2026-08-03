import streamlit as st
import pandas as pd
from applications.application_manager import ApplicationManager
from models.application import Application

def show_applications():
    if "show_add_form" not in st.session_state:
        st.session_state.show_add_form = False
    st.header("💼 Applications")
    st.caption("Track all your job applications.")
    
    manager = ApplicationManager()

    stats = manager.get_application_stats()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total", stats["Total"])

    with col2:
        st.metric("Applied", stats["Applied"])

    with col3:
        st.metric("Interview", stats["Interview"])

    with col4:
        st.metric("Offer", stats["Offer"])

    st.divider()

    
    
    applications = manager.get_all_applications()
    rows=[]
    for app in applications:
        rows.append({
            "Company": app.company,
            "Role": app.role,
            "Status": app.status,
            "Platform": app.job_platform,
            "Date Applied": app.date_applied.strftime("%d %b %Y"),
            "Follow Up Date": app.follow_up_date.strftime("%d %b %Y")
        })

    df = pd.DataFrame(rows)
    st.dataframe(df,width="stretch")

    with st.expander("➕ Add Application"):
            with st.form("application_form"):
                company = st.text_input("Company")

                role = st.text_input("Role")

                platform = st.selectbox(
                    "Platform",
                    [
                        "LinkedIn",
                        "Amazon",
                        "Company Website",
                        "Handshake",
                        "Indeed",
                        "Referral",
                        "Other"
                    ]
                )
                job_link = st.text_input("Job Link")

                status = st.selectbox(
                    "Status",
                    [
                        "Applied",
                        "OA Scheduled",
                        "OA Completed",
                        "Interview",
                        "Offer",
                        "Rejected",
                        "Withdrawn"
                    ]
                )
                submitted = st.form_submit_button("Save Application")
                if submitted:
                    if not company.strip():
                        st.warning("Company name is required.")
                    elif not role.strip():
                        st.warning("Role is required.")
                    elif not job_link.strip():
                        st.warning("Job link is required.")
                    else:
                        application = Application(
                            company=company,
                            role=role,
                            job_platform=platform,
                            job_link=job_link,
                            status=status
                        )

                        manager.add_application(application)

                        st.success("Application added successfully!")

                        st.session_state.show_add_form = False

                        st.rerun()

    

    if not applications:
        st.info("No job applications added yet.")
        return

    