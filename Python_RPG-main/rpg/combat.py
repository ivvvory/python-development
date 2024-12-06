from operator import truediv


class Combat():
    def __init__(self, player_characters, npc, player_ply_function, endgame_function):
        self.player_characters = player_characters
        self.npc = npc
        self.interactive_mode = False
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.endgame_function = endgame_function
	#are_all_characters_dead
    def characters_dead(self):
        pass

    def combat_over(self):
        pass
    
    def end_combat(self):
        pass

    def ply(self):
        pass
        
    def print_stats(self):
        pass
    
    def turn(self):
        pass

    def start(self):
        pass