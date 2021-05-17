# Todo List App

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/femiayotubosun/simple-todo-webapp/blob/main/LICENSE) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A simple todolist app written with flask.
---
To try app,

After cloning, install virtualenv if you haven't.
```
pip install virtualenv
```
Create new virtual environment and activate it.
```
virtualenv venv
.\venv\scripts\activate
```
Install requirements.
```
pip install -r requirements.txt
```

Edit .env file

```
APP_SECRET_KEY=change_to_securekey
SQLALCHEMY_DATABASE_URI=set_your_database_uri
FLASK_APP='run.py'
```
Start app

```
flask run
```
