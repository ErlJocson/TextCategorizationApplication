from pydantic import BaseModel
from typing import Optional


class MetaInfoBase(BaseModel):
    interaction_id: str
    interaction_verbatim: str
    

class MetaInfoCreate(MetaInfoBase):
    meta

class MetaInfoResponse(MetaInfoBase):
    metadata_id: str
    session_id: str
    user_id: str

    class Config:
        from_attributes = True

class MetaInfoUpdate(MetaInfoBase):
    interaction_id: Optional[str] = None
    interaction_verbatim: Optional[str] = None

    class Config:
        from_attributes = True
