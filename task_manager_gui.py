# task_manager_gui.py

import tkinter as tk
from tkinter import messagebox, simpledialog  # Add this line
from task_handler import TaskHandler

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.task_handler = TaskHandler()

        self.create_widgets()

    def create_widgets(self):
        # Task List
        self.tasks_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10)

        # Buttons
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

        toggle_button = tk.Button(self.root, text="Toggle Task", command=self.toggle_task)
        toggle_button.pack(pady=5)

        refresh_button = tk.Button(self.root, text="Refresh List", command=self.refresh_list)
        refresh_button.pack(pady=5)

        # Refresh the initial list
        self.refresh_list()

    def add_task(self):
        task_description = simpledialog.askstring("Add Task", "Enter task description:")
        task_due_date = simpledialog.askstring("Add Task", "Enter due date (format: YYYY-MM-DD):")

        new_task = {
            "description": task_description,
            "due_date": task_due_date,
            "completed": False,
        }

        self.task_handler.add_task(new_task)
        self.refresh_list()

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_handler.remove_task(task_index)
            self.refresh_list()

    def toggle_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_handler.toggle_task_status(task_index)
            self.refresh_list()

    def refresh_list(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = self.task_handler.get_tasks()

        for task in tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            self.tasks_listbox.insert(tk.END, f"{task['description']} - Due Date: {task['due_date']} - {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
