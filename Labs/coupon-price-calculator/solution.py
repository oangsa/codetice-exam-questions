item_count = int(input())
subtotal = 0.0

for _ in range(item_count):
    name, price, qty = input().split()
    subtotal += float(price) * int(qty)

coupon = input().strip()
discount = 0.0
if coupon == "SAVE10":
    discount = subtotal * 0.10
elif coupon == "SAVE50" and subtotal >= 300:
    discount = 50.0

shipping = 40.0
if subtotal >= 500 or coupon == "FREESHIP":
    shipping = 0.0

total = subtotal - discount + shipping

print(f"Subtotal: {subtotal:.2f} Baht")
print(f"Discount: {discount:.2f} Baht")
print(f"Shipping: {shipping:.2f} Baht")
print(f"Total: {total:.2f} Baht")
