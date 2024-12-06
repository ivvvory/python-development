import random
import rpg 

from rpg import Character

class Generator():
    def __init__(self):
        pass

    def character(self):
        char = Character()
        char.hit_p_max = 6
        char.intel = random.randint(3,19)
        char.race = random.choice("Human", "Elf", "Dwarf", "Ork", "Halfling")
        char.strength = random.randint(3,19)
        char.charisma = random.randint(3,19)
        char.wisdom = random.randint(3,19)
        char.dexterity = random.randint(3,19)
        char.constitution = random.randint(3,19)
        char.p_class = random.choice("Druid", "Paladin", "Warrior", "Mage", "Barbarian")
        char.level = 3
        char.hit_p_max = 10
        char.movement = (5,31)
        char.xp = 3000
        return char