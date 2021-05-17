from flask import Blueprint, render_template, request, redirect, url_for
from app.common.service import get_all, delete_one
from app.models import TodoList
from app.todo_list.forms import TodoListForm
from app.exts import db

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET', 'POST', 'DELETE'])
def index():
    todos = get_all(TodoList)
    form = TodoListForm(request.form)
    if request.method == 'POST':
        todolist = TodoList(name=form.name.data)
        db.session.add(todolist)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('index.html', todos=todos, form=form)


@main.route('/<int:todoid>', methods=['POST'])
def delete_todo(todoid):
    if request.method == 'POST':
        delete_one(TodoList, todoid)
        return redirect(url_for('main.index'))
    return redirect(url_for('todoList.get_todo', todoid=todoid))
