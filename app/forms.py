from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class TextInput(Form):
    url = TextField('foobar', validators = [Required()])