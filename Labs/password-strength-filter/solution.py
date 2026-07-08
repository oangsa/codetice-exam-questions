password_count = int(input())
strong_passwords = []
weak_passwords = []
special_chars = "!@#$%"

for _ in range(password_count):
    password = input().strip()
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:
        if "a" <= ch <= "z":
            has_lower = True
        elif "A" <= ch <= "Z":
            has_upper = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if len(password) < 8:
        weak_passwords.append((password, "Too short"))
    elif not has_lower:
        weak_passwords.append((password, "Missing lowercase"))
    elif not has_upper:
        weak_passwords.append((password, "Missing uppercase"))
    elif not has_digit:
        weak_passwords.append((password, "Missing digit"))
    elif not has_special:
        weak_passwords.append((password, "Missing special character"))
    else:
        strong_passwords.append(password)

print("Strong Passwords:")
if strong_passwords:
    for password in strong_passwords:
        print(password)
else:
    print("None")

print("Weak Passwords:")
if weak_passwords:
    for password, reason in weak_passwords:
        print(f"{password}: {reason}")
else:
    print("None")

print(f"Summary: {len(strong_passwords)} strong, {len(weak_passwords)} weak")
