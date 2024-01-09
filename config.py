# config.py

class Config(object):
    DEBUG = False
    SECRET_KEY = 'your_secret_key_here'
    PHOTOS_DIR_PATH = '/Volumes/Toshiba 1TB 2022.12.06/flickrBrowser/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/kevincameron/Documents/onelifejapan_static_2023/flaskPhotoTagger/database.db'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass
