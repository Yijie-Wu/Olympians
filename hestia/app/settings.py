import sys
from os import getenv
from os.path import dirname, join


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


BASE_DIR = dirname(dirname(__file__))
DATA_DIR = join(BASE_DIR, 'data')


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY', 'anything you want')
    IMAGE_STORE = getenv('IMAGE_STORE', DATA_DIR)

    SQLALCHEMY_DATABASE_URI = prefix + join(BASE_DIR, 'data.db')


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
