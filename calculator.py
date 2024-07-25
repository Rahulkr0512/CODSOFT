import tkinter as tk
from math import sqrt, pow

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        self.create_number_pad()
        self.create_operator_buttons()

    def create_number_pad(self):
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.', '='
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def create_operator_buttons(self):
        operators = [
            '+', '-', '*', '/',
            'sqrt', 'pow', 'clear'
        ]

        row_val = 1
        col_val = 3

        for operator in operators:
            tk.Button(self.root, text=operator, width=5, command=lambda operator=operator: self.click_operator(operator)).grid(row=row_val, column=col_val)
            row_val += 1

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def click_operator(self, operator):
        if operator == 'sqrt':
            try:
                result = sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif operator == 'pow':
            try:
                result = pow(float(self.entry.get()), 2)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif operator == 'clear':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, operator)

root = tk.Tk()
root.title("Calculator")
calc = Calculator(root)
root.mainloop()