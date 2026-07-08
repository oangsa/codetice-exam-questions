product_count = int(input())
products = {}
cart = {}

for _ in range(product_count):
    product_id, name, price, stock = input().split()
    products[product_id] = {"name": name, "price": float(price), "stock": int(stock)}

command_count = int(input())

for _ in range(command_count):
    parts = input().split()
    command = parts[0]

    if command == "ADD":
        product_id = parts[1]
        qty = int(parts[2])
        if product_id not in products:
            print(f"Failed: Product {product_id} not found.")
            continue

        product = products[product_id]
        if product["stock"] < qty:
            print(f"Failed to add {product['name']}: Insufficient stock (Only {product['stock']} left)")
            continue

        product["stock"] -= qty
        cart[product_id] = cart.get(product_id, 0) + qty
        print(f"Added {qty} {product['name']} to cart.")

    elif command == "REMOVE":
        product_id = parts[1]
        qty = int(parts[2])
        if product_id not in cart:
            print(f"Failed to remove {product_id}: Not in cart.")
            continue

        product = products[product_id]
        if cart[product_id] < qty:
            print(f"Failed to remove {product['name']}: Only {cart[product_id]} in cart.")
            continue

        cart[product_id] -= qty
        product["stock"] += qty
        if cart[product_id] == 0:
            del cart[product_id]
        print(f"Removed {qty} {product['name']} from cart.")

    elif command == "VIEW":
        print("Cart:")
        total = 0.0
        if not cart:
            print("None")
        else:
            for product_id in sorted(cart):
                product = products[product_id]
                qty = cart[product_id]
                subtotal = product["price"] * qty
                total += subtotal
                print(f"{product['name']}: {qty} x {product['price']:.2f} = {subtotal:.2f} Baht")
        if total > 1000:
            total *= 0.9
        print(f"Total: {total:.2f} Baht")
