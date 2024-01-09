from ..extensions import db

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

# class TagGroup(db.Model):
#     __tablename__ = 'tag_groups'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     tags = db.relationship('Tag', secondary=taggroups_tags, lazy='subquery',
#                            backref=db.backref('tag_groups', lazy=True))
