from models.application import Application, default_follow_up
import json
from dataclasses import asdict
from uuid import UUID
from datetime import datetime

class ApplicationStorage:
    def __init__(self):
        self.filepath = "storage/application_db/applications.json"
    def load(self) -> list[Application]:
        try:
            with open(self.filepath, "r") as file:
                data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

        applications = []

        for app_data in data:
            application = Application(
                company=app_data["company"],
                role=app_data["role"],
                job_platform=app_data["job_platform"],
                job_link=app_data["job_link"],
                resume_used=UUID(app_data["resume_used"])
                if app_data.get("resume_used") and app_data["resume_used"] != "None" else None,
                document_id=UUID(app_data["document_id"])
                if app_data.get("document_id") and app_data["document_id"] != "None" else None,
                status=app_data["status"],
                referral=app_data.get("referral"),
                location=app_data.get("location", "Remote"),
                salary_offered=app_data.get("salary_offered"),
                interview_date=datetime.fromisoformat(app_data["interview_date"])
                if app_data.get("interview_date")
                else None,
                notes=app_data.get("notes"),
                date_applied=datetime.fromisoformat(app_data["date_applied"])
                if app_data.get("date_applied")
                else datetime.now(),
                follow_up_date=datetime.fromisoformat(app_data["follow_up_date"])
                if app_data.get("follow_up_date")
                else default_follow_up(),
                application_id=UUID(app_data["application_id"]),
            )

            applications.append(application)
        return applications

    def save(self, applications: list[Application]):
        application_data = [asdict(app) for app in applications]
        for application in application_data:
            application["application_id"] = str(application["application_id"])
            application["resume_used"] = str(application["resume_used"])
            application["document_id"] = str(application["document_id"])
            application["date_applied"] = application["date_applied"].isoformat()
            application["follow_up_date"] = application["follow_up_date"].isoformat()
            if application["interview_date"] is not None:
                application["interview_date"] = application["interview_date"].isoformat()

        with open(self.filepath, "w") as file:
            json.dump(application_data, file, indent=4)

    def add(self, application: Application):
        applications = self.load()
        applications.append(application)
        self.save(applications)

    def update(self, application: Application):
        applications = self.load()
        for i, app in enumerate(applications):
            if app.application_id == application.application_id:
                applications[i] = application
                self.save(applications)
                return True 
        return False

    def delete(self, application: Application):
        applications = self.load()
        applications = [app for app in applications if app.application_id != application.application_id]
        self.save(applications)

    def get_by_id(self, application_id: UUID):
        applications = self.load()
        for app in applications:
            if app.application_id == application_id:
                return app
        return None

