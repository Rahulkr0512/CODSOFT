import tkinter as tk
from tkinter import ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.completed_tasks = []

        # Create the GUI layout
        self.task_label = tk.Label(root, text="To-Do List")
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Add", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(self.button_frame, text="Delete", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT)

        self.complete_button = tk.Button(self.button_frame, text="Complete", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(self.button_frame, text="Exit", command=root.destroy)
        self.exit_button.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack()

        self.completed_listbox = tk.Listbox(root, width=40, height=10)
        self.completed_listbox.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_tasks)
        self.save_button.pack()

        self.load_button = tk.Button(root, text="Load", command=self.load_tasks)
        self.load_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            pass

    def complete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.tasks.pop(task_index)
            self.completed_tasks.append(task)
            self.task_listbox.delete(task_index)
            self.completed_listbox.insert(tk.END, task)
        except IndexError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
            for task in self.completed_tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                self.tasks = [task.strip() for task in tasks]
                self.task_listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
