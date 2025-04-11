
# Ask the user for the amount of data in their monthly hotspot plan (in gigabytes)
data_gb = float(input("Enter the amount of data in your monthly hotspot plan (in GB): "))

# Convert gigabytes to megabytes.
# Formula for converting GB to MB is 
# 1 GB = 1,000,000,000 / 1,000,000 = 1000 MB.

data_mb = data_gb * 1000


hours_low = data_mb / 43.2
hours_normal = data_mb / 72
hours_high = data_mb / 144

# Display the calculated streaming hours
print("\nWith your data plan, you can stream music for:")
print(f"Low quality: {hours_low:.2f} hours")
print(f"Normal quality: {hours_normal:.2f} hours")
print(f"High quality: {hours_high:.2f} hours")


# Output:
# PS C:\Users\HP> & C:/Python313/python.exe c:/Users/HP/OneDrive/Desktop/computer-assignments/homework2.py
# Enter the amount of data in your monthly hotspot plan (in GB): 6

# With your data plan, you can stream music for:
# Low quality: 138.89 hours
# Normal quality: 83.33 hours
# High quality: 41.67 hours
