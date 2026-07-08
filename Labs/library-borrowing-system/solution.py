book_count = int(input())
books = {}
borrowed = {}

for _ in range(book_count):
    code, title, copies = input().split()
    books[code] = {"title": title, "copies": int(copies)}

command_count = int(input())

for _ in range(command_count):
    parts = input().split()
    command = parts[0]

    if command == "BORROW":
        member = parts[1]
        code = parts[2]
        if code not in books:
            print(f"Failed: Book {code} not found.")
            continue

        book = books[code]
        if book["copies"] == 0:
            print(f"Failed: {book['title']} is not available.")
            continue

        book["copies"] -= 1
        key = member + "|" + code
        borrowed[key] = borrowed.get(key, 0) + 1
        print(f"Success: {member} borrowed {book['title']}.")

    elif command == "RETURN":
        member = parts[1]
        code = parts[2]
        key = member + "|" + code
        if code not in books or borrowed.get(key, 0) == 0:
            print(f"Failed: {member} did not borrow {code}.")
            continue

        borrowed[key] -= 1
        books[code]["copies"] += 1
        print(f"Returned: {member} returned {books[code]['title']}.")

    elif command == "STATUS":
        print("Library Status:")
        for code in sorted(books):
            book = books[code]
            print(f"{code} {book['title']}: {book['copies']} available")
