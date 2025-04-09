
# user input for duration and weight
duration = float(input("How many minutes did you exercise??? "))
weight = float(input("What is your weight in kg??? "))

# Calculate calories burned based on MET values
calories_walking_slowly = (duration * 2 * 3.5 * weight) / 200
calories_walking = (duration * 3 * 3.5 * weight) / 200
calories_jogging = (duration * 8.8 * 3.5 * weight) / 200

# Display results
print(f"If you walked slowly, you burned {calories_walking_slowly:.2f} calories.")
print(f"If you walked, you burned {calories_walking:.2f} calories.")
print(f"If you jogged, you burned {calories_jogging:.2f} calories.")


# Output:
# PS C:\Users\HP> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/homework1.py
# How many minutes did you exercise? 8
# What is your weight in kg? 60
# If you walked slowly, you burned 16.80 calories.
# If you walked, you burned 25.20 calories.
# If you jogged, you burned 73.92 calories.

