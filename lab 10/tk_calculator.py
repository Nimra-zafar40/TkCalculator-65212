import tkinter as tk
import math

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        result = num ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    try:
        num = float(entry.get())
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator 💖")
root.configure(bg="white")
root.geometry("360x520")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bg="#f8f8f8", fg="black", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), ipadx=8, ipady=15)

button_frame = tk.Frame(root, bg="white")
button_frame.grid(row=1, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+']
]

btn_color = "#f4c2c2"
btn_fg = "#333333"

for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == 'C':
            cmd = clear
        else:
            cmd = lambda ch=char: button_click(ch)
        tk.Button(button_frame, text=char, width=6, height=2, font=("Arial", 16, "bold"),
                  bg=btn_color, fg=btn_fg, bd=0, command=cmd).grid(row=i, column=j, padx=5, pady=5)

tk.Button(button_frame, text='x²', width=6, height=2, font=("Arial", 16, "bold"),
          bg=btn_color, fg=btn_fg, bd=0, command=square).grid(row=4, column=0, padx=5, pady=5)

tk.Button(button_frame, text='√', width=6, height=2, font=("Arial", 16, "bold"),
          bg=btn_color, fg=btn_fg, bd=0, command=square_root).grid(row=4, column=1, padx=5, pady=5)

tk.Button(button_frame, text='=', width=14, height=2, font=("Arial", 16, "bold"),
          bg=btn_color, fg=btn_fg, bd=0, command=calculate).grid(row=4, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
