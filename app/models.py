from app.exts import db


class TodoList(db.Model):
    """
    Todo List Model
    """
    __tablename__ = 'todolist'

    id = db.Column(
        db.Integer, primary_key=True)

    name = db.Column(
        db.String(255),
        nullable=False
    )

    def __repr__(self):
        return f'Todo List: {self.name}'


class TodoItem(db.Model):
    """
    Todo List Item Model
    """
    __tablename__ = 'todoitem'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    task = db.Column(
        db.String(255),
        nullable=False
    )

    isCompleted = db.Column(
        db.Boolean,
        default=False
    )
    todo_list = db.relationship(
        'TodoList',
        backref="tasks"
    )

    todo_list_id = db.Column(db.Integer,
                             db.ForeignKey('todolist.id'))
