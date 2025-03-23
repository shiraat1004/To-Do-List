from ToDoList import ToDoList
from ToDoApp import ToDoApp
if __name__ == "__main__":
    todo_list = ToDoList()

    # Create the Tkinter application window
    app = ToDoApp(todo_list)
    app.mainloop()
