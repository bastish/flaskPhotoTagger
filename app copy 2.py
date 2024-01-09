# app.py
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .routes.main_routes import main_bp  # Now importing from routes package
from .config import Config
#from flaskPhotoTagger.extensions import db

app = Flask(__name__)
app.config.from_object(Config)
#db.init_app(app)

# Register blueprints
app.register_blueprint(main_bp)
# app.register_blueprint(gallery_bp)  # Uncomment and use when needed

if __name__ == "__main__":
    app.run(debug=True, port=5011)
