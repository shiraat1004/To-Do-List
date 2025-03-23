from datetime import datetime


class Task:
    def __init__(self, name, description, duedate):
        if not isinstance(duedate, datetime):
            raise TypeError('duedate must be of type datetime')
        if duedate < datetime.now():
            raise Exception("Due date cannot be earlier than now")
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not isinstance(description, str):
            raise Exception("Description must be a string")
        self.name = name
        self.description = description
        self.duedate = duedate
        self.done = False




    def __str__(self):
        status = "✔" if self.done else "❌"
        return f"Task {self.name} : Description: {self.description} Date Due: {self.duedate.strftime("%Y-%m-%d")} Status: {status}"
