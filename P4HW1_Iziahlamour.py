# Iziah Lamour
#11/12/2024
#P4HW1
# Assignment assess student ability to edit and enhance exiting programs

numgrades = int(input("How many scores do you want to enter? "))

for score in range(numgrades):
    grade = input(f"Enter score #{score + 1}: ")
    while grade < 0 or grade > 100:
        print(f"{grade} INVALID Score entered!!!! Score Should be between 0 and 100")
        grade = input(f"Enter score #{score + 1} again: ")

print("-----------Results------------")

print(f"Lowest Score: {min(grade)}")
print(f"Highest List: {max(grade)}")

average = sum(grade)/len(grade)
print(f"Scores average: {average}")


if average >= 90:
 letter_grade = "A"
elif average >= 80:
 letter_grade = "B"
elif average >= 70:
 letter_grade = "C"
elif average >= 60:
 letter_grade = "D"
elif average <= 59:
 letter_grade = "F"

print("Grade: {letter_grade}")
