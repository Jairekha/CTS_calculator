3rd part

# Create number buttons
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
