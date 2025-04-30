from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.models.base import Base

class CognitiveGoal(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    goal_type = Column(String, nullable=False)  # memory, focus, decision_making, etc.
    target_metrics = Column(JSON)  # List of metrics to track
    deadline = Column(DateTime(timezone=True))
    progress = Column(Float, default=0.0)  # 0.0 to 1.0
    status = Column(String, default="active")  # active, completed, paused
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="cognitive_goals")
    interventions = relationship("Intervention", back_populates="goal")
    
    def __repr__(self):
        return f"<CognitiveGoal {self.title}>" 