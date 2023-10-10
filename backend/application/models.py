from .database import db
from flask_security import UserMixin, RoleMixin

roles_users = db.Table('roles_users', 
                db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(80), unique = True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    fullname = db.Column(db.String, nullable = False)
    mobile_number = db.Column(db.Integer, nullable = False, unique = True)
    created_date = db.Column(db.String, nullable = False)
    updated_date = db.Column(db.String, nullable = False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) 
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    userposts = db.relationship('UserPosts', backref = 'user', lazy = True, cascade='all,delete-orphan')
    followers_list = db.relationship('Followers_List', backref = 'user', lazy = True, cascade='all,delete-orphan')
    following_list = db.relationship('Following_List', backref = 'user', lazy = True, cascade='all,delete-orphan')
    comments = db.relationship('Comments', backref='user', lazy = True, cascade='all,delete-orphan')
    likes = db.relationship('Likes', backref='user', lazy = True, cascade='all,delete-orphan')
    # profilepics = db.relationship('ProfilePics', backref = 'user', lazy = True, cascade='all,delete-orphan')
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'fullname': self.fullname,
            'email' : self.email,
            'mobile_number': self.mobile_number,
            "userposts" : [userpost.to_dict() for userpost in self.userposts],
            "followers_list": [follower.to_dict() for follower in self.followers_list],
            "following_list": [following.to_dict() for following in self.following_list]
        }

class UserPosts(db.Model):
    __tablename__ = 'userposts'
    post_id = db.Column(db.Integer, autoincrement = True, primary_key = True, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    username = db.Column(db.Text, nullable = False)
    post_img = db.Column(db.Text, nullable = False)
    img_filename = db.Column(db.Text, nullable = False)
    post_name = db.Column(db.Text, nullable = False)
    post_caption = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable = False)
    created_date = db.Column(db.Text, nullable = False)
    updated_date = db.Column(db.Text, nullable = False)
    isArchive = db.Column(db.Boolean, nullable = False, default = False)
    comments = db.relationship('Comments', backref='userposts', lazy = True, cascade='all,delete-orphan')
    likes = db.relationship('Likes', backref = 'userposts', lazy = True, cascade='all,delete-orphan')
    def to_dict(self):
        return {
            "post_id": self.post_id,
            "user_id": self.user_id,
            "username" : self.username,
            "post_name": self.post_name,
            "post_caption" : self.post_caption,
            "post_img": self.post_img,
            "created_date": self.created_date,
            "updated_date": self.updated_date,
            "isArchive": self.isArchive,
            "comments": [comment.to_dict() for comment in self.comments],
            "likes": [like.to_dict() for like in self.likes]
        }

class Comments(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("userposts.post_id"), nullable = False)
    text = db.Column(db.String, nullable = False)
    created_date = db.Column(db.String, nullable = False)
    def to_dict(self):
        return {
            "comment_id": self.comment_id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "text": self.text,
            "created_date": self.created_date,
            "username": self.user.username
        }

class Likes(db.Model):
    __tablename__ = 'likes'
    like_id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("userposts.post_id"), nullable = False)
    created_date = db.Column(db.String, nullable = False)
    def to_dict(self):
        return {
            "like_id": self.like_id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "created_date": self.created_date
        }

class Followers_List(db.Model):
    __tablename__ = 'followers_list'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    follower_id = db.Column(db.Integer, nullable = False)

    def to_dict(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "follower_id": self.follower_id
            }

class Following_List(db.Model):
    __tablename__ = 'following_list'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False, unique = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    following_id = db.Column(db.Integer, nullable = False)

    def to_dict(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "following_id": self.following_id
            }

# class ProfilePics(db.Model):
#     __tablename__ = 'profilepics'
#     profilepic_id = db.Column(db.Integer, primary_key=True, autoincrement = True, unique = True, nullable = False)
#     user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
#     profilepic_name = db.Column(db.Text, nullable=False)
#     profilepic_img = db.Column(db.LargeBinary, nullable=False)