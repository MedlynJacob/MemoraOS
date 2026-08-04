import streamlit as st
import pandas as pd
from applications.application_manager import ApplicationManager
from models.application import Application

def show_applications():
    if "show_form" not in st.session_state:
        st.session_state.show_form = False
    if "selected_application" not in st.session_state:
        st.session_state.selected_application = None
    if "edit_application" not in st.session_state:
        st.session_state.edit_application = None
    if "delete_confirmation" not in st.session_state:
        st.session_state.delete_confirmation = False
    if "message" in st.session_state:
        st.success(st.session_state.message)
        del st.session_state.message
    st.header("💼 Applications")
    st.caption("Track all your job applications.")
    if st.button("➕ Add Application"):
            st.session_state.edit_application = None
            st.session_state.show_form = True
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

    col1, col2 = st.columns([3,1])

    with col1:
        search = st.text_input(
            "🔍 Search Company",
            placeholder="Company"
        )

    with col2:
        status_filter = st.selectbox(
            "Status",
            [
                "All",
                "Applied",
                "OA Scheduled",
                "OA Completed",
                "Interview",
                "Offer",
                "Rejected",
                "Withdrawn"
            ]
        )
    sort = st.selectbox(
    "Sort By",
    [
        "Newest",
        "Oldest"
    ])
    applications = manager.get_all_applications()
    if not applications:
            st.info("No job applications added yet.")

    rows=[]
    for app in applications:
        rows.append({
        "ID": str(app.application_id),
        "Company": app.company,
        "Role": app.role,
        "Status": app.status,
        "Platform": app.job_platform,
        "Applied": app.date_applied,
        "Follow Up": app.follow_up_date
    })

    df = pd.DataFrame(rows)
    if search:
        df = df[
            df["Company"]
            .str.contains(search, case=False, na=False)
        ]
    if status_filter != "All":
        df = df[df["Status"] == status_filter]

    if sort == "Newest":
        df = df.sort_values("Applied", ascending=False)
    else:
        df = df.sort_values("Applied", ascending=True)

    df["Applied"] = df["Applied"].dt.strftime("%d %b %Y")
    df["Follow Up"] = df["Follow Up"].dt.strftime("%d %b %Y") 

    for app in applications:
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.subheader(app.company)
                st.write(app.role)

                st.caption(
                    f"{app.status} • {app.job_platform}"
                )

                st.write(
                    f"Applied: {app.date_applied.strftime('%d %b %Y')}"
                )

            with col2:
                if st.button( "👁 View",key=f"view_{app.application_id}"):
                    st.session_state.selected_application = app.application_id
                    st.rerun()
                if st.button("✏ Edit",key=f"edit_{app.application_id}"):
                    st.session_state.edit_application = app.application_id
                    st.session_state.show_form = True
                    st.rerun()

    if st.session_state.selected_application:
        application = manager.get_application_by_id(
            st.session_state.selected_application
        )

        st.divider()
        st.subheader("📋 Application Details")
        cols1, cols2= st.columns(2)
        with cols1:
            if st.button("Close Details"):
                st.session_state.selected_application = None
                st.session_state.delete_confirmation = False
                st.rerun()
        with cols2:
            if st.button("🗑 Delete Application"):
                st.session_state.delete_confirmation = True
        if st.session_state.get("delete_confirmation", False):
            st.warning(
                "Are you sure you want to delete this application?"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Yes, Delete"):

                    manager.delete_application(
                        st.session_state.selected_application
                    )

                    st.session_state.selected_application = None
                    st.session_state.edit_application = None
                    st.session_state.show_form = False
                    st.session_state.delete_confirmation = False

                    st.session_state.message = "Application deleted successfully!"

                    st.rerun()

            with col2:
                if st.button("Cancel Delete"):
                    st.session_state.delete_confirmation = False
                    st.rerun()

        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Company:** {application.company}")
            st.write(f"**Role:** {application.role}")
            st.write(f"**Platform:** {application.job_platform}")
            st.write(f"**Status:** {application.status}")

        with col2:
            st.write(f"**Referral:** {application.referral if application.referral else 'None'}")
            st.write(f"**Applied:** {application.date_applied.strftime('%d %b %Y')}")
            st.write(f"**Follow Up:** {application.follow_up_date.strftime('%d %b %Y')}")
            st.write(f"**Location:** {application.location if application.location else 'Remote'}")

        st.markdown("### 🔗 Job Link")
        st.write(application.job_link)
        st.markdown("### 📝 Notes")
        st.write(application.notes if application.notes else "No notes available.")

    editing = None
    if st.session_state.edit_application:
        editing = manager.get_application_by_id(st.session_state.edit_application)
    if st.session_state.show_form:
        if editing:
            st.subheader("✏ Edit Application")
            if st.button("Close Edit"):
                st.session_state.edit_application = None
                st.session_state.show_form = False
                st.rerun()
        else:
            st.subheader("➕ Add Application")

        with st.form("application_form"):
            company = st.text_input("Company",value=editing.company if editing else "")

            role = st.text_input("Role",value=editing.role if editing else "")

            platforms = [
                "LinkedIn",
                "Company Website",
                "Handshake",
                "Indeed",
                "Referral",
                "Other"
            ]
            platform = st.selectbox("Platform",platforms,index=platforms.index(editing.job_platform) if editing else 0)
            job_link = st.text_input("Job Link",value=editing.job_link if editing else "")
            referral = st.text_input("Referral",value=editing.referral if editing else "")
            statuses = [
                "Applied",
                "OA Scheduled",
                "OA Completed",
                "Interview",
                "Offer",
                "Rejected",
                "Withdrawn"
            ]

            status = st.selectbox("Status",statuses,index=statuses.index(editing.status) if editing else 0)
            notes = st.text_area("Notes",value=editing.notes if editing and editing.notes else "",height=120)
            location = st.text_input("Location",value=editing.location if editing else "Remote")
            button_text = "Update Application" if editing else "Save Application"
            submitted = st.form_submit_button(button_text)
            cancel = st.form_submit_button("Cancel")
            if submitted:
                if not company.strip():
                    st.warning("Company name is required.")
                elif not role.strip():
                    st.warning("Role is required.")
                elif not job_link.strip():
                    st.warning("Job link is required.")
                else:
                    if editing:
                        editing.company = company
                        editing.role = role
                        editing.job_platform = platform
                        editing.job_link = job_link
                        editing.referral = referral
                        editing.status = status
                        editing.notes = notes
                        editing.location = location

                        manager.update_application(editing)

                    else:    
                        application = Application(
                            company=company,
                            role=role,
                            job_platform=platform,
                            job_link=job_link,
                            referral=referral if referral else None,
                            status=status,
                            notes=notes if notes else None,
                            location=location
                        )

                        manager.add_application(application)

                    if editing:
                        st.success("Application updated successfully!")
                    else:
                        st.success("Application added successfully!")


                    st.session_state.edit_application = None
                    st.session_state.show_form= False
                    st.rerun()
            if cancel:
                st.session_state.show_form = False
                st.session_state.edit_application = None
                st.rerun()
