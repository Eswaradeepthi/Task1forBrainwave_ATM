import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Inventory dictionary to store product data
inventory = {}

# User Authentication (Basic Implementation)
users = {"admin": "password"}  # Pre-defined users and passwords

# Function to handle user login
def login():
    username = simpledialog.askstring("Login", "Enter username:")
    password = simpledialog.askstring("Login", "Enter password:", show="*")
    
    if username in users and users[username] == password:
        messagebox.showinfo("Login", "Login successful!")
        return True
    else:
        messagebox.showerror("Login", "Invalid credentials!")
        return False

# Add a product to the inventory
def add_product():
    product_name = entry_product_name.get()
    product_qty = entry_quantity.get()
    
    if product_name == "" or product_qty == "":
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    if not product_qty.isdigit() or int(product_qty) < 0:
        messagebox.showerror("Input Error", "Quantity must be a non-negative integer")
        return
    
    inventory[product_name] = int(product_qty)
    messagebox.showinfo("Success", f"Added {product_name} with quantity {product_qty}")
    refresh_inventory()

# Edit an existing product
def edit_product():
    product_name = entry_product_name.get()
    
    if product_name not in inventory:
        messagebox.showerror("Error", "Product not found in inventory")
        return
    
    new_qty = simpledialog.askstring("Edit Product", f"Enter new quantity for {product_name}:")
    
    if not new_qty.isdigit() or int(new_qty) < 0:
        messagebox.showerror("Input Error", "Quantity must be a non-negative integer")
        return
    
    inventory[product_name] = int(new_qty)
    messagebox.showinfo("Success", f"Updated {product_name} to quantity {new_qty}")
    refresh_inventory()

# Delete a product from the inventory
def delete_product():
    product_name = entry_product_name.get()
    
    if product_name not in inventory:
        messagebox.showerror("Error", "Product not found in inventory")
        return
    
    del inventory[product_name]
    messagebox.showinfo("Success", f"Deleted {product_name}")
    refresh_inventory()

# Generate low-stock alerts
def low_stock_alert():
    alert_message = "Low Stock Products:\n"
    for product, qty in inventory.items():
        if qty < 5:  # Threshold for low stock
            alert_message += f"{product}: {qty} left\n"
    
    if alert_message == "Low Stock Products:\n":
        messagebox.showinfo("Low Stock", "All products are sufficiently stocked.")
    else:
        messagebox.showwarning("Low Stock Alert", alert_message)

# Refresh the inventory display
def refresh_inventory():
    listbox_inventory.delete(0, tk.END)
    for product, qty in inventory.items():
        listbox_inventory.insert(tk.END, f"{product}: {qty} units")

# Main Application Window (GUI)
app = tk.Tk()
app.title("Inventory Management System")
app.geometry("400x400")

# User Authentication
if not login():
    app.destroy()

# Product Name and Quantity Input
tk.Label(app, text="Product Name:").pack()
entry_product_name = tk.Entry(app)
entry_product_name.pack()

tk.Label(app, text="Quantity:").pack()
entry_quantity = tk.Entry(app)
entry_quantity.pack()

# Buttons for Add, Edit, Delete and Alerts
tk.Button(app, text="Add Product", command=add_product).pack(pady=5)
tk.Button(app, text="Edit Product", command=edit_product).pack(pady=5)
tk.Button(app, text="Delete Product", command=delete_product).pack(pady=5)
tk.Button(app, text="Low Stock Alert", command=low_stock_alert).pack(pady=5)

# Inventory Listbox
tk.Label(app, text="Inventory List:").pack()
listbox_inventory = tk.Listbox(app, width=50)
listbox_inventory.pack()

# Start the app
app.mainloop()
