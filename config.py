import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
