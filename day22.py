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
    scores = []
    for i in range(100000):
        boss = {
            'hit_points': 58,
            'damage': 9
        }

        player = {
            'hit_points': 50,
            'armor': 0,
            'mana': 500
        }

        mana_spent, poison_timer, shield_timer, recharge_timer = 0, 0, 0, 0

        player_turn = True
        while boss['hit_points'] > 0 and player['hit_points'] > 0:
            if player_turn:
                if recharge_timer > 0:
                    player['mana'] += spells['Recharge']['mana']
                    recharge_timer -= 1
                if poison_timer != 0:
                    boss['hit_points'] -= spells['Poison']['damage']
                    poison_timer -= 1
                if shield_timer == 0:
                    player['armor'] == 0
                elif shield_timer != 0:
                    shield_timer -= 1

                spell = choice(spell_names)
                good_spell = False
                while not good_spell:  
                    spell = choice(spell_names)
                    good_spell = True
                    if spell == 'Poison' and poison_timer > 0:
                        good_spell = False
                    elif spell == 'Shield' and shield_timer > 0:
                        good_spell = False
                    elif spell == 'Recharge' and recharge_timer > 0:
                        good_spell = False

                    if player['mana'] - spells[spell]['cost'] < 0 or player['mana'] == 0:
                        good_spell = True
                        if player['mana'] < 53:
                            player['hit_points'] = 0
                        elif player['mana'] < 73:
                            spell = 'Missle'
                        elif player['mana'] < 113:
                            spell = choice(['Drain', 'Missle'])
                        elif player['mana'] < 173:
                            if shield_timer == 0:
                                spell = choice(['Drain', 'Shield', 'Missle'])
                            else:
                                spell = choice(['Drain', 'Missle'])
                        elif player['mana'] < 229:
                            if shield_timer == 0 and poison_timer == 0:
                                spell = choice(['Drain', 'Shield', 'Missle', 'Poison'])
                            elif shield_timer == 0:
                                spell = choice(['Drain', 'Missle', 'Poison'])
                            elif poison_timer == 0:
                                spell = choice(['Drain', 'Shield', 'Missle'])
                            else:
                                spell = choice(['Drain', 'Missle'])
                        


                  
                mana_spent += spells[spell]['cost']
                player['mana'] -= spells[spell]['cost']
                if player['hit_points'] > 0:
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
                if recharge_timer > 0:
                    player['mana'] += spells['Recharge']['mana']
                    recharge_timer -= 1
                if poison_timer > 0:
                    boss['hit_points'] -= spells['Poison']['damage']
                    poison_timer -= 1
                if shield_timer > 0:
                    shield_timer -= 1

                player['hit_points'] -= boss['damage']
                if shield_timer > 0:
                    player['hit_points'] += player['armor']
                player_turn = True


        if player['hit_points'] > boss['hit_points']:
            scores.append(mana_spent)
    print(min(scores))
           

def part2():
    spells = {
        'Missle': {'cost': 53, 'damage': 4},
        'Drain': {'cost': 73, 'damage': 2, 'heal' : 2},
        'Shield': {'cost': 113, 'armor': 7, 'turns' : 6},
        'Poison': {'cost': 173, 'damage': 3, 'turns': 6},
        'Recharge': {'cost': 229, 'turns': 5, 'mana': 101},
    }

    spell_names = [key for key in spells.keys()]

    min_score = 10000000
    scores = []
    for i in range(100000):
        boss = {
            'hit_points': 58,
            'damage': 9
        }

        player = {
            'hit_points': 50,
            'armor': 0,
            'mana': 500
        }

        mana_spent, poison_timer, shield_timer, recharge_timer = 0, 0, 0, 0

        player_turn = True
        while boss['hit_points'] > 0 and player['hit_points'] > 0:
            if player_turn:
                if player['hit_points'] > 0:
                    if recharge_timer > 0:
                        player['mana'] += spells['Recharge']['mana']
                        recharge_timer -= 1
                    if poison_timer != 0:
                        boss['hit_points'] -= spells['Poison']['damage']
                        poison_timer -= 1
                    if shield_timer == 0:
                        player['armor'] == 0
                    elif shield_timer != 0:
                        shield_timer -= 1

                    spell = choice(spell_names)
                    good_spell = False
                    while not good_spell:  
                        spell = choice(spell_names)
                        good_spell = True
                        if spell == 'Poison' and poison_timer > 0:
                            good_spell = False
                        elif spell == 'Shield' and shield_timer > 0:
                            good_spell = False
                        elif spell == 'Recharge' and recharge_timer > 0:
                            good_spell = False

                        if player['mana'] - spells[spell]['cost'] < 0 or player['mana'] == 0:
                            good_spell = True
                            if player['mana'] < 53:
                                player['hit_points'] = 0
                            elif player['mana'] < 73:
                                spell = 'Missle'
                            elif player['mana'] < 113:
                                spell = choice(['Drain', 'Missle'])
                            elif player['mana'] < 173:
                                if shield_timer == 0:
                                    spell = choice(['Drain', 'Shield', 'Missle'])
                                else:
                                    spell = choice(['Drain', 'Missle'])
                            elif player['mana'] < 229:
                                if shield_timer == 0 and poison_timer == 0:
                                    spell = choice(['Drain', 'Shield', 'Missle', 'Poison'])
                                elif shield_timer == 0:
                                    spell = choice(['Drain', 'Missle', 'Poison'])
                                elif poison_timer == 0:
                                    spell = choice(['Drain', 'Shield', 'Missle'])
                                else:
                                    spell = choice(['Drain', 'Missle'])
                            


                      
                    mana_spent += spells[spell]['cost']
                    player['mana'] -= spells[spell]['cost']
                    if player['hit_points'] > 0:
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
                if recharge_timer > 0:
                    player['mana'] += spells['Recharge']['mana']
                    recharge_timer -= 1
                if poison_timer > 0:
                    boss['hit_points'] -= spells['Poison']['damage']
                    poison_timer -= 1
                if shield_timer > 0:
                    shield_timer -= 1

                player['hit_points'] -= boss['damage']
                if shield_timer > 0:
                    player['hit_points'] += player['armor']
                player_turn = True
                if boss['hit_points'] > 0:
                    player['hit_points'] -= 1



        if player['hit_points'] > boss['hit_points']:
            scores.append(mana_spent)
    print(min(scores))
           

part2()