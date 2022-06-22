from loguru import logger
from fastapi import APIRouter

router = APIRouter()


@router.get('/health-check', status_code=200)
def health_check():
    logger.info('Health Check: service is alive')
    return {'status': 'ok'}
