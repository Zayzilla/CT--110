#Iziah Lamour
#10/10/24
#p2lab22
# write code that uses a dictionary to store user input and displays output to the user

cars = {"Camero": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

keys = cars

print(keys)

selected = input("Enter a vehicle to see it's mpg: ")
print()

print(f"The {selected} gets {cars[selected]} mgp.")
print()

miles = int(input(f"How many miles will you drive the {selected}? "))
print()

gas_needed = miles / cars[selected]

print(f"{gas_needed:.2f} gallon(s) of gas are needed to dric=ve the {selected} {miles} miles.")
