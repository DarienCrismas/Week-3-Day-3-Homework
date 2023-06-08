#Create a Move_Tutor Class that inherits from the Pokemon parent class.
#This class should have a list attribute that holds pokemon moves which
# should be populated with an api call to the PokeApi moves section. 
#Finally create a class method that teaches your pokemon up to 4 moves.
import requests
from time import sleep

"""
Program to teach/unteach moves to a Pokemon. Inherits from Pokemon class. 
"""


class Pokemon():

    def __init__(self, name):
        self.name = name
        self.types = []
        self.abilities = []
        self.weight = None
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name.lower()}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f"Please check pokemon name spelling and try again: {r.status_code}")
            return
        self.name = pokemon['name']
        self.types = [type_['type']['name'] for type_ in pokemon['types']]
        self.abilities = [ability['ability']['name'] for ability in pokemon['abilities']]
        self.weight = pokemon['weight']
        self.image = pokemon["sprites"]["front_default"]
        
        print(f"{self.name}'s data has been updated!")
                
    def __repr__(self):
        return f"You caught a {self.name}!"
    
class Move_Tutor(Pokemon):
    def __init__(self, name):
        self.move_list = []
        super().__init__(name)   

    def show_moves(self):
        print(self.move_list)

    def teach_move(self):
       #api req stuff 
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}/")
        if r.status_code == 200:
            pkmn = r.json()
        else: 
            print(f"Ran into an issue, please check your spelling and try again: {r.status_code}")
            return
        self.pkmn_moves = [move["move"]["name"] for move in pkmn["moves"]]

        
        print(f"Your Pokemon can learn the moves: {self.pkmn_moves}")

        #while loop, will cut off afer pkmn learns four moves
        while len(self.move_list) < 4:
            new_move = input(f"What move would you like your {self.name.title()} to learn?").lower()
            if new_move not in self.pkmn_moves:
                print(f"I'm sorry, that move isn't one your {self.name.title()} can learn. Please check your spelling and try again.")
            elif new_move in self.move_list:
                print(f"Your {self.name.title()} already knows that move!")
            elif new_move not in self.move_list:
                self.move_list.append(new_move)
                print(f"Your {self.name.title()} has learned {new_move.title()}!")
                print(f"Your {self.name.title()} currently knows: ")
                self.show_moves()

        #once while loops breaks        
        else:
            print("I'm sorry, your Pokemon cannot learn any new moves!")
            print("Please forget a move to learn any new ones.")
    
    #remove move from known moves list
    def forget_move(self):
        adios_move = input(f"What move would you like your {self.name.title()} to forget? ").lower()
        if len(self.move_list) == 0:
            print("Your Pokemon has no moves to forget! Try teaching them something first.")
        elif adios_move in self.move_list:
            self.move_list.remove(adios_move)
            print(f"Your {self.name.title()} has forgotten {adios_move.title()}!")
            print(f"Your {self.name.title()} currently knows: ")
            self.show_moves()


#try mew if you want an even worse wall of text
#mew = Move_Tutor("mew")   
#mew.teach_move()    

houndoom = Move_Tutor("houndoom")
houndoom.forget_move() #just to show the 0 condition works
sleep(1)
houndoom.teach_move()
sleep(1)
houndoom.forget_move()