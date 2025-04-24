import math

def radius(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
def circumference(r):
    return 2 * math.pi * r
def area(r):
    return math.pi * r ** 2
def main():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    
    r = radius(x1, y1, x2, y2)
    c = circumference(r)
    a = area(r)

    
    print("Radius:", r)
    print("Circumference:", c)
    print("Area:", a)

main()

# Output:
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/hw4.py
# Enter x1: 7
# Enter y1: 8
# Enter x2: 8 
# Enter y2: 9
# Radius: 1.4142135623730951
# Circumference: 8.885765876316732
# Area: 6.283185307179588
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments>