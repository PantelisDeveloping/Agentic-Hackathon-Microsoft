from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.models.base import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Cognitive profile
    chronotype = Column(String)  # morning/evening person
    baseline_focus = Column(Integer)  # 1-10
    baseline_stress = Column(Integer)  # 1-10
    baseline_energy = Column(Integer)  # 1-10
    
    # Integration settings
    fitbit_connected = Column(Boolean, default=False)
    google_calendar_connected = Column(Boolean, default=False)
    muse_connected = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<User {self.email}>" 