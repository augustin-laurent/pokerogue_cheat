
# CheatRogue

CheatRogue is a Python-based tool designed to interact with the PokeRogue API. It allows users to manipulate their game data, such as unlocking all starter Pokemon, unlocking specific Pokemon, adding gacha tickets, and more.

## Features

-   **Login**: The tool logs into the PokeRogue API using the provided username and password.
-   **Get Trainer Data**: Retrieves the trainer's data from the API.
-   **Update Trainer Data**: Updates the trainer's data on the API with the given payload.
-   **Unlock All Starters**: Unlocks all starter Pokemon in the game.
-   **Unlock Specific Pokemon**: Unlocks a specific Pokemon in the game.
-   **Add Ticket**: Adds gacha tickets to the player's account.
-   **Print Pokemon**: Prints all Pokemon in the pokedex.
-   **End Session**: Ends the current session.

## Usage

To use this tool, you need to create an instance of the  `cheatRogue`  class with your username and password. Then, you can call the methods to perform the desired actions.

from  functions  import  cheatRogue

# Create an instance

cr  =  cheatRogue("your_username",  "your_password")

# Unlock all starters

cr.unlock_all_starters()

# Unlock a specific Pokemon

cr.unlock_specific_pokemon()

# Add tickets

cr.add_ticket()

# Print all Pokemon

cr.print_pokemon()

# End the session

cr.end_session()

## Dependencies

-   `requests`: Required to make HTTP requests to the PokeRogue API.
-   `random`: Used to generate random numbers for various game data.

## Disclaimer

This tool is intended for educational purposes only. Misuse of this tool can violate the terms of service of the PokeRogue game. Please use responsibly.

## License

This project is licensed under the MIT License
