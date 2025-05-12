age = int(input("What's your age: "))


if age < 5:
    price = "Free"
elif 5 <= age <= 12:
    price = "$7.50"
elif 13 <= age <= 64:
    price = "$12.00"
else: 
    price = "$8.00"

print(f"Your ticket price is {price}")


# Output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/part2,py
# What's your age: 9
# Your ticket price is $7.50
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/part2,py
# What's your age: 87
# Your ticket price is $8.00
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/part2,py
# What's your age: 18
# Your ticket price is $12.00
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/part2,py
# What's your age: 3
# Your ticket price is Free
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments>