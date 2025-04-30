from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, JSON, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base

class Intervention(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    goal_id = Column(Integer, ForeignKey("cognitivegoal.id"))
    type = Column(String, nullable=False)  # meditation, exercise, nap, etc.
    duration = Column(Integer, nullable=False)  # in minutes
    priority = Column(Float)  # 0.0 to 1.0
    description = Column(String)
    scheduled_time = Column(DateTime(timezone=True), nullable=False)
    completed = Column(Boolean, default=False)
    completion_time = Column(DateTime(timezone=True))
    conditions = Column(JSON)  # Conditions for the intervention
    impact_metrics = Column(JSON)  # Measured impact on cognitive metrics
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="interventions")
    goal = relationship("CognitiveGoal", back_populates="interventions")
    
    def __repr__(self):
        return f"<Intervention {self.type} at {self.scheduled_time}>" 