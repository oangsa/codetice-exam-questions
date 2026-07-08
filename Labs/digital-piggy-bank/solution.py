class PiggyBank:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            return False
        self.balance -= amount
        return True


owner = input().strip()
command_count = int(input())
bank = PiggyBank(owner)

for _ in range(command_count):
    parts = input().split()
    command = parts[0]

    if command == "DEPOSIT":
        amount = float(parts[1])
        bank.deposit(amount)
        print(f"Deposited {amount:.2f} Baht to {owner}. Balance: {bank.balance:.2f} Baht.")
    elif command == "WITHDRAW":
        amount = float(parts[1])
        if bank.withdraw(amount):
            print(f"Withdrew {amount:.2f} Baht from {owner}. Balance: {bank.balance:.2f} Baht.")
        else:
            print(f"Failed: Insufficient funds in {owner}'s piggy bank.")
    elif command == "CHECK":
        print(f"Balance for {owner}: {bank.balance:.2f} Baht.")

print(f"Final Balance: {bank.balance:.2f} Baht")
