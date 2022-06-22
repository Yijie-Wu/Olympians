from loguru import logger
from fastapi import FastAPI

from app.settings import BaseConfig, get_config
from app.apis.v1 import router as v1_router
from app.events import start_event, shutdown_event


def create_app() -> FastAPI:
    config = get_config()
    app = FastAPI(**config.fastapi_kwargs)

    register_logger(config)
    register_event(app)
    register_routers(app, config)

    return app


def register_event(app: FastAPI):
    app.add_event_handler('startup', start_event)
    app.add_event_handler('shutdown', shutdown_event)


def register_routers(app: FastAPI, config: BaseConfig):
    app.router.include_router(v1_router, prefix=config.GLOBAL_API_PREFIX)


def register_logger(config: BaseConfig):
    logger.remove()
    logger.add(
        sink=config.LOGGING_SINK,
        rotation=config.LOGGING_ROTATION,
        format=config.DEFAULT_FORMAT,
        level=config.LOGGING_LEVEL,
        enqueue=config.LOGGING_ENQUEUE,
        backtrace=config.LOGGING_TRACEBACK,
        diagnose=config.LOGGING_DIAGNOSE
    )
