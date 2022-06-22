from fastapi import APIRouter

from app.apis.v1 import health_check

router = APIRouter()

router.include_router(health_check.router, prefix='/v1', tags=['Health Check'])
