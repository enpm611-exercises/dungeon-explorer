print("Welcome to Dungeon Explorer!")

player_name = input("What is your name? ")

print(f"Hello, {player_name}!")

choice = input("Would you like to go left or right? ")

if choice.lower() == "left":
    print("You enter a dark forest.")
else:
    print("You see a castle in the distance.")
