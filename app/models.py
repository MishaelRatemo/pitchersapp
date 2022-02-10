from urllib import response
from . import db
from email.policy import default

from . import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User( UserMixin, db.Model):
     # def __init__(self,email,username,password,pitchees):
    #     self.email = email
    #     self.username = username
    #     self.password=password
    #     self.pitchees = pitchees
    
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)    
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    my_pitch = db.relationship('Pitches', backref='user', lazy='dynamic')
    comment = db.relationship('Comments', backref = 'user', lazy = 'dynamic')
    upvotes = db.relationship('Upvotes', backref = 'user', lazy = 'dynamic')
    downvotes = db.relationship('Downvotes', backref = 'user', lazy = 'dynamic')
    
    
    @property
    def password(self):
        raise AttributeError('You are not allwed to read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'  


class Pitches(db.Model):
    # all_pitches=[]
    # def __ini__(self,pitch_id,owner,title,description,category,upvotes,downvotes,comments):
    #     self.pitch_id = pitch_id
    #     self.owner = owner
    #     self.title = title
    #     self.description = description
    #     self.category = category
    #     self.upvotes = upvotes
    #     self.downvotes = downvotes
    #     self.comments = comments
    
    __tablename__ = 'pitches'

    pid = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    # downvotes = db.Column(db.Integer, default=int(0))
    # upvotes = db.Column(db.Integer, default=int(0))
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comments',backref='pitch',lazy='dynamic')
    upvotes = db.relationship('Upvotes', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvotes', backref = 'pitch', lazy = 'dynamic')
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    

    
    @classmethod
    def get_pitches(cls, id):
        pitches = Pitches.query.order_by(pitch_id=id).desc().all()
        return pitches

    def __repr__(self):
        return f'Pitch {self.description}'       
        
    # def savePitches(self):
    #     Pitches.all_pitches.append(self)
        
    # @classmethod
    # def get_pitches(cls,id):
    #     response = []
    #     for pitch in cls.all_pitches:
    #         if pitch.pitch_id ==id:
    #             response.append(pitch)
    #     return response        

class Upvotes(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_u_id = db.Column(db.Integer,db.ForeignKey('pitches.pid'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()

    def add_upvotes(cls,id):
        upvote_pitch = Upvotes(user = current_user, pitch_u_id=id)
        upvote_pitch.save_upvotes()
    
    @classmethod
    def get_upvotes(cls,id):
        upvote = Upvotes.query.filter_by(pitch_u_id=id).all()
        return upvote

    @classmethod
    def get_all_upvotes(cls,pitch_id):
        upvotes = Upvotes.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_u_id}'


class Downvotes(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    pitch_d_id = db.Column(db.Integer,db.ForeignKey('pitches.pid'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_downvotes(cls,id):
        downvote_pitch = Downvotes(user = current_user, pitch_d_id=id)
        downvote_pitch.save_downvotes()

    
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvotes.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote = Downvotes.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_d_id}'      

class Comments(db.Model):
    __tablename__='comments'
    
    id = db.Column(db.Integer,primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.pid'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)

    
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"

        
        