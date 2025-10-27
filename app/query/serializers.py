from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Query(BaseModel):
    query_name: str
    description: str
    user_id: str
    session_id: str

class QueryCreate(Query):
    pass

class QueryResponse(Query):
    query_id: str
    query_created: datetime

class QueryUpdate(Query):
    query_name: Optional[str]
    description: Optional[str]
    user_id: Optional[str]
    session_id: Optional[str]

