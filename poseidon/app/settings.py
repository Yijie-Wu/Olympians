from os import getenv
from os.path import dirname, join

BASE_DIR = dirname(dirname(__file__))
DATA_DIR = join(BASE_DIR, 'data')


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY', 'anything you want')
    FILE_STORE = getenv('FILE_STORE', DATA_DIR)


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
