from Task import *
import json


class ToDoList:
    list_num = 1

    def __init__(self, name=None):
        if not name or not isinstance(name, str):
            self.name = f"ToDoList{ToDoList.list_num}"
            self.tasks = []
        else:
            self.name = name
        ToDoList.list_num += 1

    def save(self):
        tasks_data = [{"name": task.name,
                       "description": task.description,
                       "duedate": task.duedate.isoformat(),
                       "completed": task.done} for task in self.tasks]

        with open("TasksFile.json", "w") as file:
            json.dump(tasks_data, file, indent=4)

    def add_task(self, name, description, duedate):
        try:
            task = Task(name, description, datetime.strptime(duedate, "%Y-%m-%d"))
            self.tasks.append(task)
        except Exception as e:
            raise e

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                self.save()
                return True
        return False

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.done = True
                self.save()
                return True
        return False

    def print_tasks(self):
        for task in self.tasks:
            print(task)





