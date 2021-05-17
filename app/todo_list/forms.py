from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Required


class TodoForm(FlaskForm):
    task = StringField("Enter your task", validators=[
                       Required(), Length(1, 128)])
    submit = SubmitField("Add new task")


class TodoListForm(FlaskForm):
    name = StringField(
        "Enter your todolist title", validators=[Required(), Length(1, 129)])
    submit = SubmitField("Add")
