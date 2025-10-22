from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone, timedelta

PH_TZ = timezone(timedelta(hours = 8))


class SessionManagement(BaseModel):
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_name: str
    description: Optional[str] = None
    date_ceated: datetime = Field(default_factor = lambda: datetime.now(PH_TZ))
    user_id: str

class Query(BaseModel):
    query_id: str = Field(default_factory = lambda: str(uuid.uuid4()))
    query_name: str
    description: str
    date_created: datetime = Field(default_factor = lambda: datetime.now(PH_TZ))
    session_id: str


