import requests
import random

from pokemon import pokedex

class cheatRogue():

    loggedIn = False

    def __init__(self, userName: str = "", password: str = "", log: bool = True):
        """
        Initializes the class with login information.
        """
        self.s = requests.Session()
        self.loginUrl = "https://api.pokerogue.net/account/login"
        self.headers = {
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.data = { "username": userName, "password": password }
        self.loggedIn = False   
        with requests.Session() as s:
            try:
                self.auth = s.post(self.loginUrl, headers=self.headers, data=self.data).json()["token"]
                self.auth_headers = {
                    "authorization": self.auth,
                 **self.headers
                }
                self.loggedIn = True
            except :
                if log:
                    print("Error: Invalid username or password")
        
        self.pokedex = pokedex

        self.trainer_data_url = "https://api.pokerogue.net/savedata/get?datatype=0"
        self.update_trainer_data_url = "https://api.pokerogue.net/savedata/update?datatype=0"

    def get_trainer_data(self):
        """
        Retrieves the trainer's data from the API.
        """
        try: 
            data = self.s.get(self.trainer_data_url, headers = self.auth_headers).json()
            return data
        
        except Exception as e:
            print(f"Error on get_trainer_data() -> {e}")

    def update_trainer_data(self, payload):
        """
        Updates the trainer's data on the API with the given payload.
        """
        try:
            data = self.s.post(self.update_trainer_data_url, headers = self.auth_headers, json = payload)
            return data

        except Exception as e:
            print(f"Error on update_trainer_data() -> {e}")

    def unlock_all_starters(self):
        """
        Unlocks all starter Pokemon in the game.
        """
        try:
            total_caught = sum(random.randint(150, 250) for _ in range(len(self.pokedex)))
            total_seen = sum(random.randint(150, 350) for _ in range(len(self.pokedex)))

            is_shiny = int(input("Do you want Pokemons to be shiny? (1: Yes, 2: No)(number): "))
            if is_shiny == 1:
                is_shiny += 16
                shiny_types = {"Rare": 32, "Ultra rare": 64}

                for shiny_type, value in shiny_types.items():
                    flag = int(input(f"Do you want them to unlock [{shiny_type}] tier shiny? (1: Yes, 2: No)(number): "))
                    if flag == 1:
                        is_shiny += value

            for i, entry in enumerate(self.pokedex):
                data = {
                    "dexData": {
                        entry: {
                            "seenAttr": 479,
                            "caughtAttr": is_shiny,
                            "natureAttr": 67108862,
                            "seenCount": random.randint(150, 350),
                            "caughtCount": random.randint(150, 250),
                            "hatchedCount": 0,
                            "ivs": [31]*6
                        }
                    },
                    "starterData": {
                        entry: {
                            "moveset": None,
                            "eggMoves": 15,
                            "candyCount": random.randint(150, 250) + 20,
                            "abilityAttr": 7,
                            "passiveAttr": 0,
                            "valueReduction": 0
                        }
                    },
                    "gameStats": {
                        "battles": total_caught + random.randint(1, total_caught),
                        "pokemonCaught": total_caught,
                        "pokemonSeen": total_seen,
                        "shinyPokemonCaught": len(self.pokedex) * 2
                    }
                }

                self.update_trainer_data(data)

            print("All starter Pokemon has been updated!")
        except Exception as e:
            print(f"Error on unlock_all_starters() -> {e}")
    
    def unlock_specific_pokemon(self):
        """
        Unlocks a specific Pokemon in the game.
        """
        try:
            data = self.get_trainer_data()
            
            dexId = input("Which Pokemon?(Pokemon name / Pokedex ID): " )

            if dexId.isnumeric():    
                if dexId not in data["starterData"]:
                    return print(f"There's no Pokemon with the ID: {dexId}")
                
            else:
                if dexId.lower() in self.pokemon_id_by_name["dex"]:
                    dexId = self.pokemon_id_by_name["dex"][dexId]   
                else:
                    return print(f"There's no Pokemon with the Name: {dexId}")
                        
            isShiny = int(input("Do you want the Pokemon to be shiny? (1: Yes, 2: No)(number): "))
            if isShiny == 1:
                isShiny = 143
                shiny_types = {
                   "Default": 16,
                   "Rare": 32,
                   "Ultra rare": 64
                }
               
                for shiny in shiny_types:
                    flag = int(input(f"Do you want it to unlock [{shiny}] tier shiny? (1: Yes, 2: No)(number): "))
                    if flag == 1:
                        isShiny += shiny_types[shiny]
                       
            else: isShiny = 253
            seenAttr = 479
            caughtAttr = isShiny
            natureAttr = 67108862
            caught = int(input("How many of this Pokemon have you caught? (at least one) (+1 candy per)(number): "))
            hatched = int(input("How many of this pokemon have you hatched? (at least one) (+2 candy per hatch)(number): "))
            seenCount = int(input("How many of this Pokemon have you seen? (Needs to be more or equal to caught)(number): "))
            spatk_iv = int(input("What's the [special attack IV] of the Pokemon?(number): "))
            def_iv = int(input("What's the [defense IV] of the Pokemon?(number): "))
            atk_iv = int(input("What's the [attack IV] of the Pokemon?(number): "))
            hp_iv = int(input("What's the [health IV] of the Pokemon?(number): "))
            spd_iv = int(input("What's the [speed IV] of the Pokemon?(number): "))
            spdef_iv = int(input("What's the [special defense IV] of the Pokemon?(number): "))
            ivs = [spatk_iv, def_iv, atk_iv, hp_iv, spd_iv, spdef_iv]

            data["dexData"][dexId] = {
              "seenAttr": seenAttr,
              "caughtAttr": caughtAttr,
              "natureAttr": natureAttr,
              "seenCount": seenCount,
              "caughtCount": caught,
              "hatchedCount": hatched,
              "ivs": ivs
                }

            data["starterData"][dexId] = {
              "moveset": None,
              "eggMoves": 15,
              "candyCount": caught + (hatched * 2),
              "abilityAttr": 7,
              "passiveAttr": 0,
              "valueReduction": 0
                }

            self.get_trainer_data()
            self.update_trainer_data(data)
            print(f"The Pokemon with the dex entry of {dexId} has been updated!")

        except Exception as e:
            print(f"Error on starter_edit() -> {e}")
    
    def add_ticket(self):
        """
        Adds gacha tickets to the player's account.
        """      
        try:
            data = self.get_trainer_data()
            
            voucherCounts = {
                "0": int(input("How many [Common] tickets do you want to have?(number): ")),
                "1": int(input("How many [Rare] tickets do you want to have?(number): ")),
                "2": int(input("How many [Epic] tickets do you want to have?(number): ")),
                "3": int(input("How many [Legendary tickets do you want to have?(number):")) 
                }
            
            data["voucherCounts"] = voucherCounts
            self.update_trainer_data(data)
            print("Your gacha tickets has been updated!")
                
            
        except Exception as e:
            print(f"Error on add_ticket() -> {e}")

    def print_pokemon(self):
        """
        Prints all Pokemon in the pokedex.
        """
        try:
            for key, value in self.pokedex.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error on print_pokemon() -> {e}")

    def end_session(self):
        """
        Ends the current session.
        """
        try:
            self.s.close()
        except Exception as e:
            print(f"Error on end_session() -> {e}")
    