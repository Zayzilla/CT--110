# Iziah Lamour
# 9/24/2024
# P1WH1
# how to write code that collects information from user, processes information collected and display results to user.

# display output to user
print("-----Calculating Expontents----")
print()
print()

# Get info from user
base_Value = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
print()
print()

# Calculate the value of the exponent math
result= base_Value ** exponent

# display the reult of the math
print(base_Value, "raised to the power of", exponent, "is", result,"!!")
print()
print()

print("------Addition and Subtraction---------")
print()
print()

# get info from user
start_int = int(input("Enter a starting integer: "))
add_int = int(input("Enter an integer to add: "))
sub_int = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate the math
result2 = start_int + add_int - sub_int

# display the result
print(start_int, "+", add_int, "-", sub_int, "is equal to", result2)


