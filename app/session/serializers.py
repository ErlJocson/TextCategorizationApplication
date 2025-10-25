from pydantic import BaseModel
from datetime import datetime


class Session(BaseModel):
    session_name: str
    description: str
    user_id: str

class SessionCreate(Session):
    pass


class SessionResponse(Session):
    session_id: str
    date_created: datetime
