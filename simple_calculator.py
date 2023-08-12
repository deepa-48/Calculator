import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == "Add":
        result.set(num1 + num2)
    elif operation == "Subtract":
        result.set(num1 - num2)
    elif operation == "Multiply":
        result.set(num1 * num2)
    elif operation == "Divide":
        if num2 == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(num1 / num2)
    else:
        result.set("Please select a operation")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields and labels
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
result = tk.StringVar()
operation_var = tk.StringVar()
operation_var.set("Select Operation")

label_num1 = tk.Label(root, text="Enter first number:")
label_num2 = tk.Label(root, text="Enter second number:")
label_result = tk.Label(root, text="Result:")
label_operation = tk.Label(root, text="Select operation:")

# Create operation options
operation_options = ["Add", "Subtract", "Multiply", "Divide"]
option_menu = tk.OptionMenu(root, operation_var, *operation_options)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Grid layout
label_num1.grid(row=0, column=0)
entry_num1.grid(row=0, column=1)
label_num2.grid(row=1, column=0)
entry_num2.grid(row=1, column=1)
label_operation.grid(row=2, column=0)
option_menu.grid(row=2, column=1)
calculate_button.grid(row=3, column=0, columnspan=2)
label_result.grid(row=4, column=0)
tk.Label(root, textvariable=result).grid(row=4, column=1)

# Start the GUI event loop
root.mainloop()
