from datetime import datetime
import pytz
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base

PH_TZ = pytz.timezone("Asia/Manila")


def philippine_now():
    return datetime.now(PH_TZ)


class Query(Base):
    __tablename__ = 'query'

    query_id = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    query_name = Column(String(36), nullable = False)
    description = Column(String(36), nullable = False)
    date_created = Column(DateTime(timezone = True), nullable = False, default = philippine_now)
    user_id = Column(String(36), ForeignKey('user.user_id'), nullable = False)
    session_id = Column(String(36), ForeignKey('session.session_id'), nullable = False)
    
    user = relationship('User', back_populates = 'query')
    session = relationship('Session', back_populates = 'query')

