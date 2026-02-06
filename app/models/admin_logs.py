from sqlalchemy import Column, Integer, String
from .base import Base

class AdminLog(Base):
    __tablename__ = "admin_logs"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    description = Column(String)
