# password_generator.py

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Create labels and entry fields
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)

        self.length_entry = tk.Entry(master, width=5)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.include_uppercase_label = tk.Label(master, text="Include Uppercase:")
        self.include_uppercase_label.grid(row=1, column=0, padx=5, pady=5)

        self.include_uppercase_var = tk.IntVar()
        self.include_uppercase_checkbox = tk.Checkbutton(master, variable=self.include_uppercase_var)
        self.include_uppercase_checkbox.grid(row=1, column=1, padx=5, pady=5)

        self.include_numbers_label = tk.Label(master, text="Include Numbers:")
        self.include_numbers_label.grid(row=2, column=0, padx=5, pady=5)

        self.include_numbers_var = tk.IntVar()
        self.include_numbers_checkbox = tk.Checkbutton(master, variable=self.include_numbers_var)
        self.include_numbers_checkbox.grid(row=2, column=1, padx=5, pady=5)

        self.include_special_chars_label = tk.Label(master, text="Include Special Characters:")
        self.include_special_chars_label.grid(row=3, column=0, padx=5, pady=5)

        self.include_special_chars_var = tk.IntVar()
        self.include_special_chars_checkbox = tk.Checkbutton(master, variable=self.include_special_chars_var)
        self.include_special_chars_checkbox.grid(row=3, column=1, padx=5, pady=5)

        # Create generate button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Create password display label
        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.grid(row=5, column=0, padx=5, pady=5)

        self.password_display = tk.Label(master, text="", wraplength=400)
        self.password_display.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def generate_password(self):
        length = int(self.length_entry.get())
        include_uppercase = self.include_uppercase_var.get()
        include_numbers = self.include_numbers_var.get()
        include_special_chars = self.include_special_chars_var.get()

        chars = string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_numbers:
            chars += string.digits
        if include_special_chars:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_display.config(text=password)

root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()