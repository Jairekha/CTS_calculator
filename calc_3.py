import tkinter as tk

def add_to_display(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + value)

                         
def clear_display():
    entry_display.delete(0, tk.END)

def clear_all():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")
        
window = tk.Tk()
window.title("Calculator")

entry_display = tk.Entry(window, width=25, font=('Arial', 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '=', '+','C'  # Added '0' button
]

row_num = 1
col_num = 0

for button in buttons:
    if button == '=':
        tk.Button(window, text=button, width=10, command=calculate).grid(row=row_num, column=col_num, padx=5, pady=5)
    elif button == 'C':
        tk.Button(window, text=button, width=10, command=clear_all).grid(row=row_num, column=3, padx=5, pady=5)
    else:
        tk.Button(window, text=button, width=10, command=lambda b=button: add_to_display(b)).grid(row=row_num, column=col_num, padx=5, pady=5)
    
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1
        
window.mainloop()
