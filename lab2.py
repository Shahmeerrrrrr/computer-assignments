# Getting user input
cereal_name = input("Enter the name of the cereal do you like to eat: ")
calories_per_serving = float(input("Enter the number of calories per serving: "))
ounces_per_serving = float(input("Enter the number of ounces per serving: "))

# Calculating calories per ounce
calories_per_ounce = calories_per_serving / ounces_per_serving

# Displaying results
print(f"One serving of {cereal_name} is {ounces_per_serving} ounces and has {calories_per_ounce:.2f} calories per ounce.")

# Ask for daily calorie intake
daily_calories = float(input("Enter the total calories you plan to consume today with this cereal: "))

# Calculate how many ounces can be eaten
max_ounces = daily_calories / calories_per_ounce

# Display the result
print(f"To stay within {daily_calories} calories, you can eat up to {max_ounces:.2f} ounces of {cereal_name}.")


# Output
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/lab2.py
# Enter the name of the cereal do you like to eat: cheerios 
# Enter the number of calories per serving: 100
# Enter the number of ounces per serving: 2.5
# One serving of cheerios is 2.5 ounces and has 40.00 calories per ounce.
# Enter the total calories you plan to consume today with this cereal: 300
# To stay within 300.0 calories, you can eat up to 7.50 ounces of cheerios.