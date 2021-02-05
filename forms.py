import flask_ckeditor
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    author = StringField("Author Name", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Your Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    sign_in = SubmitField("Sign Me UP")

class LoginForm(FlaskForm):
    email = StringField("Your Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    sign_in = SubmitField("Sign Me IN")

class CommentForm(FlaskForm):
    comment= CKEditorField("What do you feel about the post")
    submit = SubmitField("Submit Comment")

