import tkinter as tk
from tkinter import messagebox as mb
def on_button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))
def evaluate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        mb.showerror("Error", "Invalid Expression")
def clear():
    entry.delete(0, tk.END)
def toggle_theme():
    if theme_var.get() == 'light':
        root.config(bg='#2E2E2E')
        entry.config(bg='#555555', fg='white')
        for button in button_objects:
            button.config(bg='#555555', fg='white')
        toggle_button.config(bg='#555555', fg='white', activebackground='#444444')
        theme_var.set('dark')
    else:
        root.config(bg='#FFFFFF')
        entry.config(bg='white', fg='black')
        for button in button_objects:
            button.config(bg='white', fg='black')
        toggle_button.config(bg='white', fg='black', activebackground='#DDDDDD')
        theme_var.set('light')
root = tk.Tk()
root.title("Simple Calculator made in Python")
root.geometry("800x1000")
theme_var = tk.StringVar(value='light')
entry = tk.Entry(root, font=('Cambria', 20), bg='white', fg='black', bd=10, relief='sunken', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('C', 5, 0)
]
button_objects = []
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 20), bg='white', fg='black', command=evaluate)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 20), bg='white', fg='black', command=clear)
    else:
        btn = tk.Button(root, text=text, font=('Arial', 20), bg='white', fg='black', command=lambda symbol=text: on_button_click(symbol))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button_objects.append(btn)
for row in range(6):
    root.grid_rowconfigure(row, weight=1)
for col in range(4):
    root.grid_columnconfigure(col, weight=1)
toggle_button = tk.Button(root, text="Toggle Dark/Light", font=('Arial', 12), command=toggle_theme)
toggle_button.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
toggle_theme()
root.mainloop()