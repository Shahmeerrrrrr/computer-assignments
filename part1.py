
month = int(input("What is the Month right now (1-12): "))
day = int(input("Also what is the day today (1-31): "))

if (day >= 21 and month == 3 or month == 4 or month == 5 or month == 6  and day <= 20):
    print("It is Spring")

elif (day >= 21 and month == 6 or month == 7 or month == 8 or month == 9 and day <= 22):
    print("It is Summer")

elif (day >= 23 and month == 9 or month == 10 or month == 11 or month == 12 and day <= 21):
        print("It is Fall")

else:
    print("It is Winter")        
    

# Output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/part1.py
# What is the Month right now (1-12): 6
# Also what is the day today (1-31): 21
# It is Summer
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> 

