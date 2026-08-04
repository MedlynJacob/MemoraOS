import streamlit as st
from applications.application_manager import ApplicationManager


def show_dashboard():

    st.header("🏠 Dashboard")
    st.caption("Overview of your job search progress.")

    manager = ApplicationManager()

    stats = manager.get_application_stats()

    st.subheader("📊 Application Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info(f""" ### {stats["Total"]} Total Applications""")

    with col2:
        st.info(f""" ### {stats["Applied"]} Applications Sent""")

    with col3:
        st.warning(f""" ### {stats["Interview"]} Interviews""")

    with col4:
        st.success(f""" ### {stats["Offer"]} Offers""")

    st.divider()


    st.subheader("📈 Pipeline")

    statuses = [
        "Applied",
        "OA Scheduled",
        "OA Completed",
        "Interview",
        "Offer",
        "Rejected",
        "Withdrawn"
    ]

    applications= manager.get_all_applications()


    if not applications:
        st.info("No applications tracked yet")
        return

    counts={}

    for status in statuses:
        counts[status]=len([app for app in applications if app.status == status])

    for status, count in counts.items():
        st.write(f"**{status}**")
        st.progress(count / max(stats["Total"],1))
        st.caption(f"{count} applications")
