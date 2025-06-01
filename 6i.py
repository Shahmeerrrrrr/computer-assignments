my_list = []


for i in range(8):
    num = int(input(f"Enter integer #{i+1}: "))
    my_list.append(num)
def filter_evens(numbers):
    print("Even numbers!!!:", end=" ")
    for num in numbers:
        if num % 2 == 0: 
            print(num, end=" ")
    print() 

filter_evens(my_list)
# Output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/6i.py
# Enter integer #1: 2
# Enter integer #2: 9
# Enter integer #3: 4
# Enter integer #4: 8
# Enter integer #5: 5
# Enter integer #6: 3
# Enter integer #7: 0
# Enter integer #8: 7
# Even numbers!!!: 2 4 8 0 