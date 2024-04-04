
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
        
# Create number buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '=', '+','C'  # Added '0' button
]

row_num = 1
col_num = 0

