from flask import Blueprint, render_template, request, url_for, redirect
from app.common.service import get_one, delete_one
from app.models import TodoList, TodoItem
from app.todo_list.forms import TodoForm
from app import db

todoList = Blueprint('todoList', __name__, template_folder='templates')


@todoList.route('/', methods=['GET'])
def get_todos():
    return redirect(url_for('main.index'))


@todoList.route('/<int:todoid>', methods=['GET', 'POST'])
def get_todo(todoid):
    form = TodoForm(request.form)
    todo = get_one(TodoList, todoid)
    if request.method == 'POST':
        task = form.task.data
        new_item = TodoItem(task=task)
        new_item.todo_list = todo
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('todoList.get_todo', todoid=todoid))

    return render_template('todolist.html', todo=todo, form=form)


@todoList.route('<int:todoId>/clearComplete', methods=['POST'])
def clear_todo(todoId):
    todo_list = get_one(TodoList, todoId)
    for task in todo_list.tasks:
        if(task.isCompleted):
            delete_one(TodoItem, task.id)
            print("here")
    return redirect(url_for('todoList.get_todo'))


@todoList.route('<int:todoId>/items/<int:itemId>/toggle', methods=['PATCH'])
def get_home(todoId,  itemId):
    item = get_one(TodoItem, itemId)
    item.isCompleted = not item.isCompleted
    db.session.commit()
    return {
        "message": "succcess"
    }
