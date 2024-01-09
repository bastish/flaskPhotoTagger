
from ..extensions import db

# Association table for the many-to-many relationship between Photos and Tags
photos_tags = db.Table('photos_tags',
    db.Column('photo_id', db.Integer, db.ForeignKey('photos.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

# Association table for the many-to-many relationship between TagGroups and Tags
taggroups_tags = db.Table('taggroups_tags',
    db.Column('taggroup_id', db.Integer, db.ForeignKey('tag_groups.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)
