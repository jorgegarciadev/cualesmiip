from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class TextInput(Form):
    url = TextField('url', default = 'twitter.com', validators = [Required()])
