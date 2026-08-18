def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            item, quantity = order.split(":")
            if ":" not in order:
                print(f"Invalid format: {order}")
                continue
            quantity = int(quantity)
            if quantity < 0:
                print(f"Negative quantity not allowed: {order}")
                continue
            cart[item] = cart.get(item, 0) + quantity
            
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")
 

    # Return the completed cart
    return cart

result = handle_shopping_cart(["butter:2","honey:4","almond","juice:3"])

print(result)  # Should print {'apple': 3, 'banana': 2, 'milk': 5}
