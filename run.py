from functions import cheatRogue
import sys

while cheatRogue.loggedIn == False:
    try:
        print("\n PokeRogue Account")
        username = input("\t Username : ")
        password = input("\t Password : ")
        rogue = cheatRogue(userName=username, password=password, log=False)
        if rogue.loggedIn == False:
            print("\n Incorrect login information, check if the server is up and try login again.")
    except KeyboardInterrupt:
        print("\n\n Exiting script...")
        sys.exit()

print(f"Successfully logged in as: {username}")

while True:
    print("<------------------------- COMMANDS ------------------------>")
    print("\t 1 : Print all Pokemons with their ID")
    print("\t 2 : Unlock all starters [With perfects ivs and 3 shiny forms on your choice]")
    print("\t 3 : Unlock a specific Pokemon")
    print("\t 4 : Add ticket to your account")
    print("\t 5 : End script")
    command = int(input("Enter a command: "))
    if command == 1:
        rogue.print_pokemon()
    elif command == 2:
        rogue.unlock_all_starters()
    elif command == 3:
        rogue.unlock_specific_pokemon()
    elif command == 4:
        rogue.add_ticket()
    elif command == 5:
        rogue.end_session()
        break
    else:
        print("Invalid command, try again.")