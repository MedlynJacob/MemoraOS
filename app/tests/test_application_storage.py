from applications.application_storage import ApplicationStorage
from models.application import Application
from uuid import uuid4


def test_application_storage():

    storage = ApplicationStorage()

    # Create fake application
    application = Application(
        company="Amazon",
        role="Software Development Engineer",
        job_platform="LinkedIn",
        resume_used=uuid4(),
        job_link="https://amazon.jobs/example",
        document_id=uuid4()
    )

    print("\n--- Adding Application ---")
    storage.add(application)

    # Load applications
    applications = storage.load()

    print("\n--- Loaded Applications ---")
    for app in applications:
        print(app)

    assert len(applications) > 0

    # Get application by ID
    retrieved_application = storage.get_by_id(application.application_id)

    print("\n--- Retrieved Application ---")
    print(retrieved_application)

    assert retrieved_application is not None
    assert retrieved_application.company == "Amazon"


    # Update application status
    print("\n--- Updating Status ---")

    application.status = "OA Scheduled"

    updated = storage.update(application)

    assert updated is True


    # Verify update
    updated_application = storage.get_by_id(application.application_id)

    print("\n--- After Update ---")
    print(updated_application)

    assert updated_application.status == "OA Scheduled"


    # Delete application
    print("\n--- Deleting Application ---")

    storage.delete(application)

    deleted_application = storage.get_by_id(application.application_id)

    assert deleted_application is None

    print("\n✅ Application Storage Test Passed!")


if __name__ == "__main__":
    test_application_storage()