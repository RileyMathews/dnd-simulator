import random

class Dragislav():
    def calculate_damage_for_round(self, armor_class, round):
        hit_this_round = False
        total_damage_for_round = 0
        for i in range(2):
            hit = self.roll_to_hit(armor_class)
            if hit != "miss":
                total_damage_for_round += self.calculate_hit_damage(hit, hit_this_round, round)
                hit_this_round = True
        return total_damage_for_round
            
            
    def calculate_hit_damage(self, hit, hit_this_round, round):
        damage = 0
        if hit_this_round == False: # this is the first hit this round
            if round < 5: # zepher strike can be used
                damage += random.randint(1, 8)
            else: # assume hunters mark has been cast
                damage += random.randint(1, 6)
        # bow damage
        damage += random.randint(1, 8)
        # damage up to now has been dice damage, double for crit
        if hit == "crit":
            damage = damage * 2
        # bow modifier
        damage += 4
        return damage

    def roll_to_hit(self, armor_class):
        hit_roll = random.randint(1, 20) + 9
        if hit_roll == 20:
            return "crit"
        elif hit_roll >= armor_class:
            return "hit"
        else:
            return "miss"

