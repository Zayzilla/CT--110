import random

# Function to create a hero character
def create_hero():
    name = "Bob"
    health = random.randint(70, 200)  # Corrected randit to randint
    inventory = []
    weapon = ["sword"]
    strength = random.randint(70, 200)  # Corrected randit to randint
    
    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Weapons": weapon,
        "Strength": strength
    }
    return character

# Function to create a villain character
def create_villain():
    name = "Evil Tim"
    health = random.randint(70, 200)  # Corrected randit to randint
    inventory = []
    weapon = ["nunchucks"]
    strength = random.randint(70, 200)  # Corrected randit to randint
    
    character = {
        "Name": name,
        "Health": health,
        "Items": inventory,
        "Weapons": weapon,
        "Strength": strength
    }
    return character

def display_character_info(character):
    print(f"Name: {character['Name']}")
    print(f"Health: {character['Health']}")
    print(f"Strength: {character['Strength']}")
    print(f"Items: {', '.join(character['Items'])}")  # Display items
    print(f"Weapons: {', '.join(character['Weapons'])}")  # Display weapons
    print("------")

# Battle function
def battle(hero, villain):
    while hero["Health"] > 0 and villain["Health"] > 0:
        # Randomly choose who attacks
        characters = [hero, villain]
        random.shuffle(characters)
        attacker = characters[0]
        defender = characters[1]

        # Print the names of attacker and defender
        print(f'{attacker["Name"]} attacks {defender["Name"]}!')
        
        # Calculate damage
        damage = random.randint(5, 20)
        defender["Health"] -= damage  # Deduct damage from defender's health
        print(f'{defender["Name"]} takes {damage} damage. Health left: {defender["Health"]}')
        
        # Check if anyone has won
        if hero["Health"] <= 0:
            print(f"{hero['Name']} has been defeated! {villain['Name']} wins!")
            return villain
        elif villain["Health"] <= 0:
            print(f"{villain['Name']} has been defeated! {hero['Name']} wins!")
            return hero

        print("------ Next Round ------")
    
    return None  # If somehow both characters are still alive, return None

def main():
    print("Game is starting...")
    
    # Create characters
    hero = create_hero()
    villain = create_villain()

    print(f"\nHero: {hero['Name']} (Health: {hero['Health']})")
    print(f"Villain: {villain['Name']} (Health: {villain['Health']})\n")

    # Start the battle
    winner = battle(hero, villain)

    if winner:
        print(f"\nThe winner is: {winner['Name']}")

if __name__ == "__main__":
    main()
