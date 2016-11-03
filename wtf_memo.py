import flask
from flaks import flask_wtf
from flask_wtf import Form
from wtforms import TextField

class MemoForm(Form):
   name = TextField("Memo")