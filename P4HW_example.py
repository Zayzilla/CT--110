#similar to P4HW1

#List of available items (not in HW)
availableitmes = ["Basketball ", "soccerball", "tennisball", "apples", "grapes", "oranges", "kiwis", "strawberry"]

# get number of items to purchase
numitems = int(input("How many items will you purchase?"))

cart = []

#loop to get the items
for item in range(numitems):
    thisitem = input(f"Enter item #{item + 1}: ")
    # Loop to ensure thisitem is an availableitems
    while thisitem not in availableitems:
        print(f"{thisitem} is not in stock")
        thisitem = input(f"Enter item #{item + 1} again: ")
#Add the valid item to the cart
cart.append(thisitem)

#loop to print each item in the cart
print("items we purchased")
for product in cart:
    print(product) 