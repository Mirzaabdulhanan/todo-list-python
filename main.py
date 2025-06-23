import tkinter as tk
from tkinter import messagebox, simpledialog, colorchooser
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimalist To-Do List")
        self.root.geometry("400x600")
        self.tasks = []
        self.load_tasks()
        
        self.dark_mode = False
        self.create_widgets()
        self.update_theme()

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, bg="white", fg="black", font=("Arial", 12))
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(fill=tk.X)

        self.task_entry = tk.Entry(self.entry_frame, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.RIGHT)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(fill=tk.X)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(fill=tk.X)

        self.toggle_button = tk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        self.toggle_button.pack(fill=tk.X)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_text = self.task_listbox.get(selected_task_index)
            new_task_text = simpledialog.askstring("Edit Task", "Edit your task:", initialvalue=task_text)
            if new_task_text:
                self.tasks[selected_task_index[0]] = new_task_text
                self.update_task_list()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
        self.save_tasks()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        self.update_theme()

    def update_theme(self):
        if self.dark_mode:
            self.root.config(bg="black")
            self.task_listbox.config(bg="gray", fg="white")
            self.add_button.config(bg="darkgray", fg="black")
            self.edit_button.config(bg="darkgray", fg="black")
            self.delete_button.config(bg="darkgray", fg="black")
            self.toggle_button.config(bg="darkgray", fg="black")
        else:
            self.root.config(bg="white")
            self.task_listbox.config(bg="white", fg="black")
            self.add_button.config(bg="lightgray", fg="black")
            self.edit_button.config(bg="lightgray", fg="black")
            self.delete_button.config(bg="lightgray", fg="black")
            self.toggle_button.config(bg="lightgray", fg="black")

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
