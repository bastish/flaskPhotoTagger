from ..extensions import db

from .association import photos_tags, taggroups_tags

class TagGroup(db.Model):
    __tablename__ = 'tag_groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tags = db.relationship('Tag', secondary=taggroups_tags, lazy='subquery',
                           backref=db.backref('tag_groups', lazy=True))
