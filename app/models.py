from . import db

class Poem(db.Model):
    __tablename__ = 'poem'

    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100), nullable=False)
    content = db.Column('content', db.String(100), nullable=False)
    author = db.Column('author', db.String(20), nullable=False)
    category = db.Column('category', db.String(20))

    def __init__(self, title, content, author, category):
        self.title = title
        self.content = content
        self.author = author
        self.category = category

    def __repr__(self):
        return '<Poem %r' % self.title
        
