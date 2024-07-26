import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack(fill="both", expand=True)

        # Create task list frame
        self.task_list_frame = ttk.Frame(self.main_frame)
        self.task_list_frame.pack(fill="both", expand=True)

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame, font=("Arial", 12), bg="#f0f0f0")
        self.task_list.pack(fill="both", expand=True)

        # Create entry frame
        self.entry_frame = ttk.Frame(self.main_frame, padding=10)
        self.entry_frame.pack(fill="x")

        # Create task entry
        self.task_entry = ttk.Entry(self.entry_frame, font=("Arial", 12), width=40)
        self.task_entry.pack(fill="x", side="left", expand=True)

        # Create button frame
        self.button_frame = ttk.Frame(self.entry_frame)
        self.button_frame.pack(side="left")

        # Create add task button
        self.add_task_button = ttk.Button(self.button_frame, text="Add Task", command=self.add_task, bootstyle="success")
        self.add_task_button.pack(side="top", fill="x")

        # Create delete task button
        self.delete_task_button = ttk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bootstyle="danger")
        self.delete_task_button.pack(side="top", fill="x")

        # Create clear all tasks button
        self.clear_all_tasks_button = ttk.Button(self.button_frame, text="Clear All Tasks", command=self.clear_all_tasks, bootstyle="warning")
        self.clear_all_tasks_button.pack(side="top", fill="x")

        # Create mark as completed button
        self.mark_as_completed_button = ttk.Button(self.button_frame, text="Mark as Completed", command=self.mark_as_completed, bootstyle="info")
        self.mark_as_completed_button.pack(side="top", fill="x")

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert("end", task)
            self.task_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete")

    def clear_all_tasks(self):
        self.tasks = []
        self.task_list.delete(0, "end")

    def mark_as_completed(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            self.tasks[task_index] = f"[Completed] {task}"
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, self.tasks[task_index])
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to mark as completed")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()