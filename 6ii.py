car_sales_data = [7, 3, 6, 0, 14, 8, 1, 2, 9, 8]

total_cars = sum(car_sales_data)
print(f"Total number of cars sold by dealership is!!: {total_cars}")


max_sales = max(car_sales_data)
top_salesperson = car_sales_data.index(max_sales) + 1  
print(f"Salesperson {top_salesperson} sold the most cars.")
print(f"Number of cars sold by him: {max_sales}")

# OUTPUT
# PS C:\Users\HP\OneDrive\Desktop\computer-assignments> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/6ii.py
# Total number of cars sold by dealership is!!: 58
# Salesperson 5 sold the most cars.
# Number of cars sold by him: 14