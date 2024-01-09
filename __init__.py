# flaskPhotoTagger/__init__.py
from flask import Flask
from .extensions import db, migrate
from .config import Config
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from .models import Photo
    from .models import Tag    
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from .routes import main_bp, gallery_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(gallery_bp)

    return app
