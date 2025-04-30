from fastapi import APIRouter
from app.api.api_v1.endpoints import (
    auth,
    users,
    cognitive_goals,
    interventions,
    digital_twin,
    wearables
)

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(cognitive_goals.router, prefix="/goals", tags=["cognitive goals"])
api_router.include_router(interventions.router, prefix="/interventions", tags=["interventions"])
api_router.include_router(digital_twin.router, prefix="/digital-twin", tags=["digital twin"])
api_router.include_router(wearables.router, prefix="/wearables", tags=["wearables"]) 