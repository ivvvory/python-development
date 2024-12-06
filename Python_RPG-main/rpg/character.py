import json

class Character():
    def __init__(self):
        self.name = "Luna"
        self.strength = 0
        self.intel = 0
        self.wisdom = 0
        self.dexterity = 0
        self.constitution = 0
        self.charisma = 0
        self.race = ""
        self.p_class = 0
        self.level = 0
        self.hit_p_max = 0
        self.movement = 0
        self.armors = []
        self.weapons = []
        self.xp = 0
        self.type = ""
        self.current_weapon = ""
        self.current_armor = ""

    def load_from_json(self, path):
        with open(path) as f:
            c = json.load(f)
        self.name = c.get("name")
        self.charisma = c.get("charisma")
        self.intel = c.get("intel")
        self.wisdom = c.get("wisdom")
        self.dexterity = c.get("dexterity")
        self.constitution = c.get("constitution")
        self.race = c.get("race")
        self.p_class = c.get("p_class")
        self.level = c.get("level")
        self.hit_p_max = c.get("hit_p_max")
        self.movement = c.get("movement")
        self.xp = c.get("xp")


    def set_current_weapon(self):
        pass
    
    def roll_to_hit(self):
        pass

    def roll_for_damage(self):
        pass

    def get_ac(self):
        pass

    def get_movement(self):
        pass

    def get_ability_bonuses(self):
        pass