from flask import Flask, render_template, send_file
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
import os

from models import db, Photo, Tag, TagGroup  # Import the database models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables if they don't exist


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def home():
    photos_path = app.config["PHOTOS_PATH"]
    galleries = [name for name in os.listdir(photos_path) if os.path.isdir(os.path.join(photos_path, name))]
    
    return render_template('index.html', galleries=galleries)

    return f"Hello, Flask! {photos_path} <br> {galleries}"
@app.route('/gallery/<gallery_name>')
def gallery_view(gallery_name):
    base_path = '/Volumes/Toshiba 1TB 2022.12.06/flickrBrowser/'
    thumbnails_path = os.path.join(base_path, gallery_name, 'images/thumbnails')
    photos_path = os.path.join(base_path, gallery_name, 'images')
    
    thumbnails = [os.path.join(gallery_name, 'images/thumbnails', name) for name in os.listdir(thumbnails_path) if name.endswith('.jpg')]
    photos = [os.path.join(gallery_name, 'images', name) for name in os.listdir(photos_path) if name.endswith('.jpg')]
    
    images = zip(thumbnails, photos)
    
    return render_template('gallery.html', gallery_name=gallery_name, images=images)

@app.route('/image/<path:filename>')
def send_image(filename):
    image_path = os.path.join('/Volumes/Toshiba 1TB 2022.12.06/flickrBrowser/', filename)
    return send_file(image_path)




@app.route('/debug')
def debug_mode():
    if app.config["DEBUG"]:
        return "Debug mode is on!"
    else:
        return "Debug mode is off."

if __name__ == '__main__':
    app.run(debug=True, port=5011)
