import streamlit as st
from applications.application_manager import ApplicationManager


def show_dashboard():

    st.header("🏠 Dashboard")
    st.caption("Overview of your job search progress.")

    manager = ApplicationManager()

    stats = manager.get_application_stats()

    st.subheader("Application Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Applications",
            stats["Total"]
        )

    with col2:
        st.metric(
            "Applied",
            stats["Applied"]
        )

    with col3:
        st.metric(
            "Interviews",
            stats["Interview"]
        )

    with col4:
        st.metric(
            "Offers",
            stats["Offer"]
        )


    st.divider()


    st.subheader("Recent Applications")

    applications = manager.get_all_applications()


    if not applications:
        st.info("No applications yet.")
        return


    for app in applications[-5:]:

        st.write(
            f"""
            **{app.company}**
            
            Role: {app.role}

            Status: {app.status}

            Applied: {app.date_applied.strftime("%d %b %Y")}
            """
        )