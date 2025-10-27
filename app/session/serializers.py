from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Session(BaseModel):
    session_name: str
    description: str
    user_id: str

class SessionCreate(Session):
    pass


class SessionResponse(Session):
    session_id: str
    date_created: datetime


class SessionUpdate(Session):
    session_name: Optional[str]
    description: Optional[str]
    user_id: Optional[str]
