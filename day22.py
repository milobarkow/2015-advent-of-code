from random import choice

def part1():
    spells = {
        'Missle': {'cost': 53, 'damage': 4},
        'Drain': {'cost': 73, 'damage': 2, 'heal' : 2},
        'Shield': {'cost': 113, 'armor': 7, 'turns' : 6},
        'Poison': {'cost': 173, 'damage': 3, 'turns': 6},
        'Recharge': {'cost': 229, 'turns': 5, 'mana': 101},
    }

    spell_names = [key for key in spells.keys()]

    min_score = 10000000
    while True:
        boss = {
            'hit_points': 58,
            'damage': 9
        }

        player = {
            'hit_points': 50,
            'armor': 0,
            'mana': 500
        }

        mana_spent = 0

        poison_timer = 0
        shield_timer = 0
        recharge_timer = 0

        player_turn = True
        while boss['hit_points'] > 0 and player['hit_points'] > 0:
            if player_turn:
                if recharge_timer > 0:
                    player['mana'] += spells['Recharge']['mana']
                    recharge_timer -= 1
                if shield_timer == 0:
                    player['armor'] == 0

                good_spell = False
                while not good_spell:  
                    spell = choice(spell_names)
                    good_spell = True
                    if spell == 'Poison' and poison_timer > 0:
                        good_spell = False
                    elif spell == 'Sheild' and shield_timer > 0:
                        good_spell = False
                    elif spell == 'Recharge' and recharge_timer > 0:
                        good_spell = False

                mana_spent += spells[spell]['cost']
                player['mana'] -= spells[spell]['cost']
                if spell == 'Missle':
                    boss['hit_points'] -= spells[spell]['damage']
                elif spell == 'Drain':
                    boss['hit_points'] -= spells[spell]['damage']
                    player['hit_points'] += spells[spell]['heal']
                elif spell == 'Shield':
                    player['armor'] += spells[spell]['armor']
                    shield_timer = spells[spell]['turns']
                elif spell == 'Poison':
                    poison_timer = spells[spell]['turns']
                else:
                    recharge_timer = spells[spell]['turns']
                player_turn = False
            else:
                if shield_timer != 0:
                    shield_timer -= 1
                if poison_timer != 0:
                    boss['hit_points'] -= spells['Poison']['damage']
                    poison_timer -= 1
                boss_attack_damage = boss['damage'] - player['armor']
                player['hit_points'] -= boss_attack_damage
                player_turn = True

        if player['hit_points'] > 0:
            temp_score = min(mana_spent, min_score)
            if temp_score != min_score:
                min_score = temp_score
                print(min_score)

           

part1()