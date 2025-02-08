import tkinter as tk
from tkinter import messagebox

def calculate_netprice():
    try:
        price = float(price_entry.get())
        discount = float(discount_entry.get())

        if not (0 <= discount <= 100):
            raise ValueError('Discount should be between 0 and 100')
        if price < 0:
            raise ValueError('Price should be greater than 0')

        net_price = price * (1 - discount / 100)
        result_label.config(text=f'Net price = {net_price:.2f}')

    except ValueError as e:
        messagebox.showerror('Error', e)
    except:
        messagebox.showerror('Error', 'Please enter valid numbers')

# Create main window
root = tk.Tk()
root.title('Net Price Calculator')
root.geometry("400x200")

# Price widgets
price_label = tk.Label(root, text='Price ($):')
price_label.pack(pady=5)
price_entry = tk.Entry(root)
price_entry.pack(pady=5)

# Discount widgets
discount_label = tk.Label(root, text='Discount (%):')
discount_label.pack(pady=5)
discount_entry = tk.Entry(root)
discount_entry.pack(pady=5)

# Calculate button
calculate_btn = tk.Button(root, text='Calculate', command=calculate_netprice)
calculate_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text='Net price = ')
result_label.pack(pady=5)

# Run the application
root.mainloop()