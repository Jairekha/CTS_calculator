# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create entry display
entry_display = tk.Entry(window, width=25, font=('Arial', 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
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
