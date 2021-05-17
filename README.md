# Todo List App
### A simple Todo List Web App with the Flask python
  

To use app, 

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
