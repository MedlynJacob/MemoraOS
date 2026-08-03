from dataclasses import dataclass,field
from datetime import datetime, timedelta
from uuid import UUID
from uuid import uuid4

def generate_id():
    return uuid4()

def default_follow_up():
    return datetime.now() + timedelta(days=14)

@dataclass
class Application:
    company: str
    role: str
    job_platform: str #Linkedin, Indeed, Handshake etc
    job_link: str
    resume_used: UUID | None = None # Resume's document ID
    document_id: UUID | None = None # Job Description ID

    status: str = "Applied" # Includes "Applied", "OA Scheduled","OA Completed","Interview" "Offer", "Rejected", "Withdrawn"
    referral: str | None = None
    location: str= "Remote"
    salary_offered: float | None = None
    interview_date: datetime | None = None 
    notes: str | None = None
    
    date_applied: datetime = field(default_factory=datetime.now)
    follow_up_date: datetime = field(default_factory=default_follow_up)
    application_id: UUID = field(default_factory=generate_id)
