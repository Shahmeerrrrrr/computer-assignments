import random

alpha = [0] * 50
for i in range(25):
    alpha[i] = i**2
for i in range(25, 50):
    alpha[i] = 3 * i


print("Initial list:")
for i in range(0, 50, 10):
    print(alpha[i:i+10])


for i in range(50):
    alpha[i] = random.randint(1, 100)

print("\nList with random numbers (1-100):")
for i in range(0, 50, 10):
    print(alpha[i:i+10])

average = sum(alpha) / len(alpha)
print(f"\nAverage: {average}")


count_100 = alpha.count(100)
print(f"Number of 100s: {count_100}")

#OUTPUT
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/lab8
# Initial list:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# [100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# [400, 441, 484, 529, 576, 75, 78, 81, 84, 87]
# [90, 93, 96, 99, 102, 105, 108, 111, 114, 117]
# [120, 123, 126, 129, 132, 135, 138, 141, 144, 147]

# List with random numbers (1-100):
# [72, 17, 97, 3, 44, 39, 44, 94, 38, 55]
# [95, 9, 61, 1, 63, 98, 94, 50, 59, 65]
# [90, 67, 84, 81, 93, 25, 56, 51, 57, 81]
# [24, 67, 56, 5, 56, 33, 93, 30, 28, 2]
# [13, 32, 71, 78, 31, 50, 50, 61, 75, 61]

# Average: 53.98
# Number of 100s: 0
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments>