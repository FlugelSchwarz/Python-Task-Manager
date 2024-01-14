## task_handler.py

import json
import os
from datetime import datetime

class TaskHandler:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists("tasks.json") and os.stat("tasks.json").st_size != 0:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        else:
            print("No tasks found or the file is empty.")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    def get_tasks(self):
        return self.tasks

    def toggle_task_status(self, task_index):
        self.tasks[task_index]["completed"] = not self.tasks[task_index]["completed"]
        self.save_tasks()
        print("Task status updated successfully!")

    def remove_task(self, task_index):
        removed_task = self.tasks.pop(task_index)
        self.save_tasks()
        print(f"Task removed: {removed_task['description']}")
