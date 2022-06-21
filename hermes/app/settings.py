import os
from enum import Enum
from functools import lru_cache
from typing import Dict, Any, Optional, Type

from pydantic import SecretStr, BaseSettings


class EnvTypes(Enum):
    dev: str = 'dev'
    prod: str = 'prod'
    test: str = 'test'


class BaseConfig(BaseSettings):
    APP_ENV: EnvTypes = EnvTypes.prod
    DEBUG: bool = False
    SERVICE_NAME: str = 'Hermes [Notification Services]'
    TITLE: str = 'Hermes Services REST APIs'
    VERSION: str = '1.0'
    DESCRIPTION: str = 'Provided apis for notification'
    SECRET_KEY = SecretStr
    DATABASE_URI: Optional[str] = None

    GLOBAL_API_PREFIX = '/api'

    DEFAULT_FORMAT: str = '{time:YYYY-MM-DD HH:mm:ss} | {level} | {process.name} | {thread.name} | {module}:{file}:{function}():{line} -> {message}'
    LOGGING_FORMAT: str = os.getenv('LOGGING_FORMAT', DEFAULT_FORMAT)
    LOGGING_LEVEL: str = os.getenv('LOGGING_LEVEL', 'INFO')
    LOGGING_TRACEBACK: bool = False
    LOGGING_ENQUEUE: bool = True
    LOGGING_DIAGNOSE: bool = True
    LOGGING_ROTATION: str = '100 MB'
    LOGGING_SINK: str = 'hermes.log'

    class Config:
        env_file = '.env'
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            'debug': self.DEBUG,
            'title': self.TITLE,
            'version': self.VERSION,
            'description': self.DESCRIPTION
        }


class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True
    DATABASE_URI: Optional[str] = None
    LOGGING_LEVEL: str = 'INFO'
    LOGGING_TRACEBACK: bool = True


class ProductConfig(BaseConfig):
    DEBUG: bool = False


class TestConfig(BaseConfig):
    DEBUG: bool = True
    DATABASE_URI: Optional[str] = None
    LOGGING_LEVEL: str = 'DEBUG'
    LOGGING_TRACEBACK: bool = True


environments: Dict[EnvTypes, Type[BaseConfig]] = {
    EnvTypes.dev: DevelopmentConfig,
    EnvTypes.prod: ProductConfig,
    EnvTypes.test: TestConfig
}


@lru_cache()
def get_config() -> BaseConfig:
    app_env = BaseConfig().APP_ENV
    config = environments[app_env]
    return config()
