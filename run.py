from app import create_app
import os

# create database
if not os.path.exists('./todoDB.db'):
    import sqlite3
    sqlite3.connect('todoDB.db')

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)
