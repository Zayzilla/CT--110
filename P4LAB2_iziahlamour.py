#Iziah Lamour
#11/7/2024
#Use loops to show positive tables
run_again = 'yes'
while run_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        for item in range(1, 13):
            print(f" {user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")
        
    run_again = input("Would you like to run the program again?")
print("Program has ended")
