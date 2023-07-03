from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False, unique=True)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
     
    @validates('name')
    def validate_name(self, key, authors):
        if not 2 <= len(authors)<50:
            raise ValueError("Name should be between two to fifty characters")
        return authors
    
    @validates('phone_number')
    def validates_phone_number(self, key, phone_number):
        if not 10 <= len(phone_number):
            raise ValueError("Phone number must have at least ten digits.")
        return phone_number
    
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    @validates('title')
    def validates_title(self, key, title):
        if not 3<=len(title)<25 :
            raise ValueError("Title length is invalid )")
        return title 
    
    @validates ('content','summary')
    def validates_content(self, key, post):
        if (key== 'content'):
            if  len(post)<=250:
                raise TypeError ("Content must be greater than or equal to 250 characters long.")
        if (key=='summary'):
            if len(post) >=250:
                raise ValueError("summary must be less than or equal to 250 characters long")
            return post
    
    @validates('category')
    def validate_category(self, key, category):
        valid_categories = ['Fiction', 'Non-Fiction']
        if category not in valid_categories:
            raise ValueError('Post category must be Fiction or Non-Fiction.')
        return category
    
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
