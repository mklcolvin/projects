def add_item(item, price, stock):  
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item] = {"price": float(price), "stock": int(stock)}
        print(f"Item '{item}' added successfully.")   
    return inventory 

def update_stock(item, quantity):
    if item in inventory:
        before_stock = inventory[item]["stock"]
        if before_stock + int(quantity) < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]["stock"] += int(quantity)
            print(f"Stock for '{item}' updated successfully.")
    else:
        print(f"Error: Item '{item}' not found.") 

    return inventory

def check_availability(item):
    if item in inventory:
        return inventory[item]["stock"]
    else:
        return f"Item not found."
    
def sales_report(sales):
    report = {}
    total = 0
    for item, quantity in sales.items():
        if item in inventory:
            if inventory[item]["stock"] >= quantity:
                report[item] = inventory[item]["price"] * quantity
                inventory[item]["stock"] -= quantity
            else:
                print(f"Error: Insufficient stock for '{item}'.")
        else:
            print(f"Error: Item '{item}' not found.")
    total = sum(report.values())
    print(f"Total revenue: ${total:.2f}")
    return report   

inventory = {}
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
sales_report(sales)  # Should output: 19.0
print(inventory)