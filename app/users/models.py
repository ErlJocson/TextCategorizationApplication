import pytz
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from app.database import Base


PH_TZ = pytz.timezone("Asia/Manila")

def philippine_now():
    return datetime.now(PH_TZ)

class User(Base):
    __tablename__ = "user"

    user_id         = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    username        = Column(String(100), nullable = False)
    email           = Column(String(100), nullable = False)
    date_created    = Column(DateTime(timezone = True), nullable = False, default = philippine_now)
    role            = Column(String(100), nullable = False)
    password        = Column(String(100), nullable = False)
    
    sessions        = relationship("Session", back_populates = 'user', cascade = 'all, delete')
    queries         = relationship("Query", back_populates = "user", cascade = 'all, delete')
    metainfos       = relationship('MetaInfo', back_populates = 'user', cascade = 'all, delete')


