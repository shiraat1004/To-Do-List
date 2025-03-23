import tkinter as tk
from tkinter import messagebox


class ToDoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list
        self.title("To-Do List")
        self.geometry("600x400")

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self, width=70, height=15)
        self.task_listbox.pack(pady=5)

        # Add Task Button
        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Complete Task Button
        self.complete_button = tk.Button(self, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Delete Task Button
        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Update the listbox with current tasks
        self.update_task_listbox()

    def add_task(self):
        def save_task():
            name = task_name_entry.get()
            description = task_desc_entry.get()
            due_date = task_due_entry.get()

            if name and description and due_date:
                self.todo_list.add_task(name, description, due_date)
                self.update_task_listbox()
                add_window.destroy()
            else:
                messagebox.showerror("Input Error", "Please fill in all fields")

        # Create a new window to input task details
        add_window = tk.Toplevel(self)
        add_window.title("Add Task")
        add_window.geometry("300x300")

        tk.Label(add_window, text="Task Name:").pack(pady=5)
        task_name_entry = tk.Entry(add_window, width=30)
        task_name_entry.pack(pady=5)

        tk.Label(add_window, text="Description:").pack(pady=5)
        task_desc_entry = tk.Entry(add_window, width=30)
        task_desc_entry.pack(pady=5)

        tk.Label(add_window, text="Due Date (YYYY-MM-DD):").pack(pady=5)
        task_due_entry = tk.Entry(add_window, width=30)
        task_due_entry.pack(pady=5)

        save_button = tk.Button(add_window, text="Save Task", command=save_task)
        save_button.pack(pady=10)

    def complete_task(self):
        complete_window = tk.Toplevel(self)
        complete_window.title("Complete Task")
        complete_window.geometry("300x300")
        tk.Label(complete_window, text="Task Name:").pack(pady=5)
        task_name_entry = tk.Entry(complete_window, width=30)
        task_name_entry.pack(pady=5)

        def on_complete_button_click():
            task_name = task_name_entry.get()
            if task_name:
                if self.todo_list.complete_task(task_name):
                    complete_window.destroy()  # Close the window after completion
                else:
                    messagebox.showerror("Input Error", "Task not found.")
            else:
                messagebox.showerror("Input Error", "Please enter a task name.")

            # Button to trigger task completion

        complete_button = tk.Button(complete_window, text="Complete Task", command=on_complete_button_click)
        complete_button.pack(pady=10)
        self.update_task_listbox()

    def delete_task(self):
        delete_window = tk.Toplevel(self)
        delete_window.title("Delete Task")
        delete_window.geometry("300x300")
        tk.Label(delete_window, text="Task Name:").pack(pady=5)
        task_name_entry = tk.Entry(delete_window, width=30)
        task_name_entry.pack(pady=5)

        def on_delete_button_click():
            task_name = task_name_entry.get()
            if task_name:
                if self.todo_list.delete_task(task_name):
                    self.update_task_listbox()
                    delete_window.destroy()  # Close the window after completion
                else:
                    messagebox.showerror("Input Error", "Task not found.")
            else:
                messagebox.showerror("Input Error", "Please enter a task name.")

        delete_button = tk.Button(delete_window, text="Delete Task", command=on_delete_button_click)
        delete_button.pack(pady=10)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, str(task))
