from models.application import Application
from applications.application_storage import ApplicationStorage
from uuid import UUID


class ApplicationManager:

    def __init__(self):
        self.storage = ApplicationStorage()


    def add_application(self, application: Application):
        self.storage.add(application)


    def update_application_status(self, application_id: UUID, status: str):
        application = self.storage.get_by_id(application_id)

        if application is None:
            return False

        application.status = status

        return self.storage.update(application)

    def get_all_applications(self):
        return self.storage.load()

    def get_by_status(self, status: str):
        applications = self.storage.load()

        return [
            app for app in applications
            if app.status == status
        ]

    def get_application_stats(self):
        applications = self.storage.load()
        stats = {
            "Total": len(applications),
            "Applied": 0,
            "OA Scheduled": 0,
            "OA Completed": 0,
            "Interview": 0,
            "Offer": 0,
            "Rejected": 0,
            "Withdrawn": 0
        }
        for app in applications:
            if app.status in stats:
                stats[app.status] += 1

        return stats
    
    def get_application_by_id(self, application_id: UUID):
        return self.storage.get_by_id(application_id)