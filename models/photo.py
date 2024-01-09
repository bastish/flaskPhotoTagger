from ..extensions import db
from .association import photos_tags


class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String, nullable=False)
    tags = db.relationship('Tag', secondary=photos_tags, lazy='subquery',
                          backref=db.backref('photos', lazy=True))
