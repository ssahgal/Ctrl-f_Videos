from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class controlf(FlaskForm):
    
    youtube_link = StringField('Youtube Link', validators=[DataRequired()])
    keyword = StringField('Keyword', validators=[DataRequired()])
    submit = SubmitField('Submit')
