import pytz
from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MetaInfo(Base):
    __tablename__ = 'metainfo'

    metainfo_id = Column(String(36), primary_key = True, default = lambda: str(uuid.uuid4()))
    interaction_id = Column(String(100), nullable = False)
    interaction_verbatim = Column(String(500), nullable = False)
    session_id = Column(String(36), ForeignKey('session.session_id'), nullable = False)
    user_id = Column(String(36), ForeignKey('user.user_id'), nullable = False)    
    
    sessions = relationship("Session", back_populates = 'metainfos')
    user = relationship('User', back_populates = 'metainfos')
    queries = relationship('Query', back_populates = 'metainfos', cascade = 'all, delete')

