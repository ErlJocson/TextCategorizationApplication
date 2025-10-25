from pydantic import BaseModel
from datetime import datetime

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



