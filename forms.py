from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired


# WTForm for creating a selection
class SelectionForm(FlaskForm):
    selection = SelectField(lable='Chose', choices="", validators=[DataRequired()])
    submit = SubmitField("Submit")


    # WTForm book form
class BookForm(FlaskForm):
    book = StringField("Book", validators=[DataRequired()])
    book_id = IntegerField("Book ID")
    chapter = StringField("Book Chapter")
    submit = SubmitField("Submit")