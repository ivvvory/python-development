from rpg.character import Character
from rpg.weapon import Weapon
from rpg.armor import Armor
from utils.generator import Generator

luna = Character()
luna.load_from_json("characters/luna.json")
print(luna.name, luna.charisma, luna.strength, luna.intel, luna.wisdom, luna.dexterity, luna.constitution, luna.race, luna.p_class, luna.level, luna.hit_p_max, luna.movement, luna.xp)

dagger = Weapon()
print(dagger.name)
dagger.load("weapons/daggers.json")
print(dagger.name)

chainmail = Armor()
print(chainmail.name)
chainmail.load("armor/chainmail.json")
print(chainmail.name)
