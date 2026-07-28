from applications.application_manager import ApplicationManager
from models.application import Application
from uuid import uuid4


def test_application_manager():

    manager = ApplicationManager()

    application = Application(
        company="Google",
        role="Software Engineer",
        job_platform="LinkedIn",
        resume_used=uuid4(),
        job_link="https://careers.google.com/example",
        document_id=uuid4()
    )

    print("\n--- Adding Application Through Manager ---")

    manager.add_application(application)


    print("\n--- Updating Status Through Manager ---")

    updated = manager.update_application_status(
        application.application_id,
        "Interview"
    )

    assert updated is True


    updated_application = manager.storage.get_by_id(
        application.application_id
    )

    print("\n--- Updated Application ---")
    print(updated_application)


    assert updated_application.status == "Interview"

    print("\n--- Getting All Applications ---\n")

    applications = manager.get_all_applications()

    for app in applications:
        print(app)

    assert len(applications) > 0

    print("\n--- Interview Applications ---\n")

    interviews = manager.get_by_status("Interview")

    for app in interviews:
        print(app)

    assert len(interviews) > 0
    print("\n--- Application Statistics ---")

    stats = manager.get_application_stats()

    print(stats)

    assert stats["Interview"] > 0

    print("\n✅ Application Manager Test Passed!")



if __name__ == "__main__":
    test_application_manager()