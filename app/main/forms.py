from click import option
from flask_wtf import FlaskForm
from wtforms import RadioField,StringField,PasswordField,SubmitField, TextAreaField,BooleanField, ValidationError
from wtforms.validators import InputRequired,Email, EqualTo

class Pitch(FlaskForm):
    pitch_title = StringField('Title', validators=[InputRequired()])
    pitch_descrip = TextAreaField('Your pitch goes here ', validators=[InputRequired()])
    pitch_category = StringField('Label', options=[('Life','Coding','Business', 'Love','Others')])
    submit = SubmitField('Submit')
    
class Comment(FlaskForm):
    Comment_decrip =TextAreaField("Comment", validators=[InputRequired()])
    submit = SubmitField('Submit Comment')
    
class Upvote(FlaskForm):
    submit =SubmitField()

class Downvote(FlaskForm):
    submit =SubmitField()