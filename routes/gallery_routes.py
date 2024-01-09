from flask import Blueprint, current_app, render_template, send_file
import os

gallery_bp = Blueprint('gallery_bp', __name__)

@gallery_bp.route('/gallery/<gallery_name>')
def gallery_view(gallery_name):
    # Access the configuration
    base_path = current_app.config.get('PHOTOS_DIR_PATH', '/default/path/if/not/set')
    
    thumbnails_path = os.path.join(base_path, gallery_name, 'images/thumbnails')
    photos_path = os.path.join(base_path, gallery_name, 'images')
    
    thumbnails = [os.path.join(gallery_name, 'images/thumbnails', name) for name in os.listdir(thumbnails_path) if name.endswith('.jpg')]
    photos = [os.path.join(gallery_name, 'images', name) for name in os.listdir(photos_path) if name.endswith('.jpg')]
    
    images = zip(thumbnails, photos)
    
    return render_template('gallery.html', gallery_name=gallery_name, images=images)

@gallery_bp.route('/image/<path:filename>')
def send_image(filename):
    image_path = os.path.join('/Volumes/Toshiba 1TB 2022.12.06/flickrBrowser/', filename)
    return send_file(image_path)
