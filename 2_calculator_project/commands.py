import tkinter as tk

curr_op = {
    "number": 0,
    "operation": None,
    "in_operation_mode": False
}

def insert_number(entry, number):
    return lambda: entry.insert(tk.END, number)

def clear_field(entry):
    def cb():
        entry.delete(0, tk.END)
        curr_op["number"] = 0
        curr_op["operation"] = None
        curr_op["in_operation_mode"] = False
    return cb

def fire_prev_operation(entry):
    number = float(entry.get())
    entry.delete(0, tk.END)
    match curr_op["operation"]:
        case "+":
            curr_op["number"] += number
        case "-":
            curr_op["number"] -= number
        case "*":
            curr_op["number"] *= number
        case "/":
            curr_op["number"] /= number
        case _:
            curr_op["number"] = number
    curr_op["operation"] = None

def operation_command(entry, operation=None):
    def cb():
        if not curr_op["in_operation_mode"]:
            fire_prev_operation(entry)
        curr_op["operation"] = operation
        curr_op["in_operation_mode"] = True
    return cb

def equal_command(entry):
    def cb():
        fire_prev_operation(entry)
        entry.insert(0, curr_op["number"])
        curr_op["number"] = 0
        curr_op["operation"] = None
        curr_op["in_operation_mode"] = False
    return cb