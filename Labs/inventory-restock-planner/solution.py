product_count = int(input())
total_units_needed = 0

print("Restock Report:")
for _ in range(product_count):
    name, stock, minimum, target = input().split()
    stock = int(stock)
    minimum = int(minimum)
    target = int(target)

    if stock < minimum:
        needed = target - stock
        total_units_needed += needed
        print(f"{name}: Order {needed} units")
    else:
        print(f"{name}: OK")

print(f"Total Units Needed: {total_units_needed}")
