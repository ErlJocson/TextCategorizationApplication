from datetime import datetime
import pytz
import uuid
from sqlalchemy import Column, String, Datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


PH_TZ = pytz.timezone("Asia/Manila")


def philippine_now():
    return datetime.now(PH_TZ)


class Session(Base):
    __tablename__ = "session"

    session_id      = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    session_name    = Column(String(100), nullable = False)
    description     = Column(String(100), nullable = True)
    date_created    = Column(Datetime(timezone = True), nullable = False, default = philippine_now)
    user_id         = Column(String(36), ForeignKey('user.user_id'), nullable = False)

    user            = relationship("User", back_populates = "session")
    query           = relationship("Query", back_populates = "session", cascade = 'all, delete')

