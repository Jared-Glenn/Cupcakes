from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class CupcakeForm(FlaskForm):
    """Form for adding cupcakes."""
    
    flavor = StringField("Cupcake Flavor")
    size = StringField("Size",
                       validators=[AnyOf(values=["Large", "Medium", "Small"])])
    rating = FloatField("Rating out of 10")
    image = StringField("Image URL",
                validators=[Optional(), URL()])
    
