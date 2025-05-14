import tkinter as tk

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


root = tk.Tk()
root.title("Calculator 💖")
root.configure(bg="white")
root.geometry("420x500")
root.resizable(False, False)


entry = tk.Entry(root, font=("Arial", 24), bg="#f8f8f8", fg="black", bd=0, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=(10, 5))


button_frame = tk.Frame(root, bg="white")
button_frame.pack()


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
        tk.Button(button_frame, text=char, width=5, height=2, font=("Arial", 16, "bold"),
                  bg=btn_color, fg=btn_fg, bd=0, command=cmd).grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=10)

equal_btn = tk.Button(root, text='=', font=("Arial", 18, "bold"), bg=btn_color, fg=btn_fg,
                      bd=0, command=calculate)
equal_btn.pack(fill="both", ipadx=5, ipady=15, padx=10, pady=(5, 10))


root.mainloop()
