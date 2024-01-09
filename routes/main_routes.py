from flask import Blueprint, render_template, current_app
from .gallery_routes import gallery_view
import os

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def main():
    photos_path = current_app.config["PHOTOS_DIR_PATH"]
    galleries = [name for name in os.listdir(photos_path) if os.path.isdir(os.path.join(photos_path, name))]
    return render_template('index.html', galleries=galleries)
