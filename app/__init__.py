from flask import Flask
from app.exts import db
from app.main.routes import main
from app.todo_list.routes import todoList


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    # register blueprints
    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(todoList, url_prefix='/todolist')
    return app


def register_extensions(app):
    db.init_app(app)
    from app import models
    db.create_all(app=app)
