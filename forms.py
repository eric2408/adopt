from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = SelectField("Pet Species", choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')])
    photo_url = StringField("Pet photo link",
                            validators=[Optional(), URL()])
    age = IntegerField("Age",
                        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes",
                        validators=[Optional(), Length(min=15)])

class EditPetForm(FlaskForm):
    """Edit Form for adding pets."""

    photo_url = StringField("Pet photo link",
                            validators=[Optional(), URL()])
    notes = TextAreaField("Notes",
                        validators=[Optional(), Length(min=15)])
    available = BooleanField("Pet available?")

