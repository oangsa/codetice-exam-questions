movie = input().strip()
seat_limit = int(input())
request_count = int(input())
prices = {"CHILD": 80, "ADULT": 120, "SENIOR": 90, "VIP": 250}
tickets_sold = 0
revenue = 0

for _ in range(request_count):
    customer, ticket_type, qty_text = input().split()
    qty = int(qty_text)

    if tickets_sold + qty > seat_limit:
        print(f"Failed: Not enough seats for {customer}.")
        continue

    cost = prices[ticket_type] * qty
    tickets_sold += qty
    revenue += cost
    print(f"{customer} booked {qty} {ticket_type} ticket(s). Cost: {cost} Baht.")

print(f"Summary for {movie}:")
print(f"Tickets Sold: {tickets_sold}/{seat_limit}")
print(f"Revenue: {revenue} Baht")
