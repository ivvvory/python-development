import json

class Weapon(): 
    def __init__(self):
        #l_d = low damage
        #h_d = high damage
        self.name = "No Weapon"
        self.price = 0
        self.weight = 0
        self.size = 0
        self.l_d = 1
        self.h_d = 4
        #everything is 0 because if theres no weapon there is nothing :)
        #and I have no idea what the basic levels of damage are because I've not played enough D&D

    def load(self, path): 
        with open(path) as f:
            weapon = json.load(f)
        self.name = weapon.get("name")

        print(weapon)
        self.name = weapon.get("name")
        self.price = weapon.get("price")
        self.weight = weapon.get("weight")
        self.size = weapon.get("size")
        self.l_d = weapon.get("damage")[0]
        self.h_d = weapon.get("damage")[1]