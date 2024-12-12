#Iziah Lamour
#10/1/24
#P2HW1
#create a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
print()

# Ask user to enter their budget
Budget = int(input("Enter Budget:"))
print()

#Ask user to enter travel destination
Destination = input("Enter your travel destination:")
print()

#Ask user for amount they will spend on gas
Gas_price = int(input("How much do you think you will spend on gas?"))
print()

#Ask user for amount they will spend on accommodation
Hotel_cost = int(input("Approximately, how much will you need for accomodation/hotel?"))
print()

#Ask user for amount they will spend on food
Food_cost = int(input("Last, how much do you need for food?"))
print()

print("-----------Travel Expenses---------")
print(f"{'Location:':<20}{Destination}")
print(f"{'Initial Budget:':<20}${Budget:,.2f}")
print(f"{'Fuel:':<20}${Gas_price:,.2f}")
print(f"{'Accomodation:':<20}${Hotel_cost:,.2f}")
print(f"{'Food:':<20}${Food_cost:,.2f}")
print("-" * 40)
print()
#Subtract expenses from budget
Remaining_Bal = Budget - Gas_price - Hotel_cost - Food_cost

#Display Results
print(f"{'Remaining Balance:':<20}${Remaining_Bal:,.2f}")


                      
                

