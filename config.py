# config.py

class Config(object):
    DEBUG = False
    SECRET_KEY = 'your_secret_key_here'
    PHOTOS_PATH = '/Volumes/Toshiba 1TB 2022.12.06/flickrBrowser/'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
