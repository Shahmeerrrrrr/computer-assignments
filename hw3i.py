balance = float(input("Enter your starting balance: $"))
transactions = int(input("How many transactions did you make? "))

deposits = 0
withdrawals = 0

for i in range(1, 4):
    while True:
        type = input(f"\nTransaction {i}: Enter 'w' for withdrawal or 'd' for deposit: ").strip().lower()
        if type in ('w', 'd'):
            break
        print("Invalid input! Please enter 'w' or 'd'.")

    amount = float(input("Enter amount: $"))

    if type == 'w':
        balance -= amount
        withdrawals += amount
    else:
        balance += amount
        deposits += amount

    print(f"Current balance: ${balance:.2f}")

print("\nFinal balance iss: ${:.2f}".format(balance))
print("Total withdrawal: ${:.2f}".format(withdrawals))
print("Total deposit: ${:.2f}".format(deposits))

# Output:
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/hw3i.py
# Enter your starting balance: $6000
# How many transactions did you make? 3

# Transaction 1: Enter 'w' for withdrawal or 'd' for deposit: w
# Enter amount: $800
# Current balance: $5200.00

# Transaction 2: Enter 'w' for withdrawal or 'd' for deposit: d
# Enter amount: $400
# Current balance: $5600.00

# Transaction 3: Enter 'w' for withdrawal or 'd' for deposit: w
# Enter amount: $4000
# Current balance: $1600.00

# Final balance iss: $1600.00
# Total withdrawal: $4800.00
# Total deposit: $400.00
