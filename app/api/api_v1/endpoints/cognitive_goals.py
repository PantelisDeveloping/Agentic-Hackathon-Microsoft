from fastapi import APIRouter, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

router = APIRouter()

class GoalType(str, Enum):
    MEMORY = "memory"
    FOCUS = "focus"
    DECISION_MAKING = "decision_making"
    EMOTIONAL_REGULATION = "emotional_regulation"
    CREATIVITY = "creativity"

class CognitiveGoalBase(BaseModel):
    title: str
    description: str
    goal_type: GoalType
    target_metrics: List[str]
    deadline: datetime

class CognitiveGoalCreate(CognitiveGoalBase):
    pass

class CognitiveGoal(CognitiveGoalBase):
    id: int
    created_at: datetime
    updated_at: datetime
    progress: float
    status: str

    class Config:
        from_attributes = True

# In-memory storage for demonstration
goals_db = []
goal_id_counter = 1

@router.post("/", response_model=CognitiveGoal)
async def create_goal(goal: CognitiveGoalCreate):
    global goal_id_counter
    new_goal = CognitiveGoal(
        id=goal_id_counter,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        progress=0.0,
        status="active",
        **goal.model_dump()
    )
    goals_db.append(new_goal)
    goal_id_counter += 1
    return new_goal

@router.get("/", response_model=List[CognitiveGoal])
async def read_goals():
    return goals_db

@router.get("/{goal_id}", response_model=CognitiveGoal)
async def read_goal(goal_id: int):
    for goal in goals_db:
        if goal.id == goal_id:
            return goal
    raise HTTPException(status_code=404, detail="Goal not found")

@router.put("/{goal_id}", response_model=CognitiveGoal)
async def update_goal(goal_id: int, goal_update: CognitiveGoalCreate):
    for i, goal in enumerate(goals_db):
        if goal.id == goal_id:
            updated_goal = CognitiveGoal(
                id=goal_id,
                created_at=goal.created_at,
                updated_at=datetime.utcnow(),
                progress=goal.progress,
                status=goal.status,
                **goal_update.model_dump()
            )
            goals_db[i] = updated_goal
            return updated_goal
    raise HTTPException(status_code=404, detail="Goal not found")

@router.delete("/{goal_id}")
async def delete_goal(goal_id: int):
    for i, goal in enumerate(goals_db):
        if goal.id == goal_id:
            del goals_db[i]
            return {"message": "Goal deleted successfully"}
    raise HTTPException(status_code=404, detail="Goal not found") 