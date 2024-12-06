import json

class Armor(): 
    def __init__(self):
        self.name = "No Armor"
        self.price = 0
        self.weight = 0
        self.ac = 11

    def load(self, path): 
        with open(path) as f:
            armors = json.load(f)
        self.name = armors.get("name")

        print(armors)
        self.name = armors.get("name")
        self.price = armors.get("price")
        self.weight = armors.get("weight")
        self.ac = armors.get("ac")
        