from sqlalchemy import String, Integer, Column, DateTime, func
from src.database import Base


class QueueStatus(Base):
    __tablename__ = 'queue_statuses'

    id = Column(Integer, primary_key=True, index=True)
    s_name = Column(String)
    c_name = Column(String)
    c_id = Column(String)
    a_type = Column(String)
    direction = Column(String)
    activation = Column(String)
    c_state = Column(String)
    control = Column(String)
    created_at = Column(DateTime, server_default=func.now())
