from distutils.command.config import config
from distutils.debug import DEBUG
import os

class Config:
    pass

class ProdConfig(Config):
    pass


class DeveConfig(Config):
    DEBUG = True
    
config_options = {
    'development' : DeveConfig,
    'production'  : ProdConfig
}