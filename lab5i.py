file = open("transaction.txt", "r")
balance = float(file.readline())
lines = file.readlines()
file.close()

print(f"Starting balance: ${balance:.2f}")
for i in range(0, len(lines), 2):
    transactions = lines[i].strip()
    amount = float(lines[i + 1].strip())

    if transactions == 'W':
        balance -= amount
    elif transactions == 'D':
        balance += amount
        
        print(f"{transactions} ${amount:.2f} Balance: ${balance:.2f}")


print(f"Final balance: ${balance:.2f}")

# output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/lab5i.py
# Starting balance: $5000.00
# D $90.00 Balance: $4050.00
# D $100.00 Balance: $4150.00
# D $1000.00 Balance: $5150.00
# Final balance: $5130.00
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments>