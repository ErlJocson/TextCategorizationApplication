from datetime import datetime
import pytz
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
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
    published = Column(String(10), nullable = False)
    
    user_id = Column(String(36), ForeignKey('user.user_id'), nullable = False)
    metainfo_id = Column(String(36), ForeignKey('metainfo.metainfo_id'), nullable = False)

    user = relationship('User', back_populates = 'queries')
    metainfos = relationship('MetaInfo', back_populates = 'queries')
