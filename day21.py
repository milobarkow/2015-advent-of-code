from itertools import combinations


def battle(player, boss):
    player_turn = True
    player_hit_points = 100
    boss_hit_points = boss['HitPoints']
    while player_hit_points > 0 and boss_hit_points > 0:
        if player_turn:
            damage = player['damage'] - boss['armor']
            if damage <= 0:
                damage = 1
            boss_hit_points -= damage
            player_turn = False
        else:
            damage = boss['damage'] - player['armor']
            if damage <= 0:
                damage = 1
            player_hit_points -= damage
            player_turn = True

    return player_hit_points > 0


def part1():
    boss = {
        'HitPoints': 103,
        'damage': 9,
        'armor': 2
    }

    shop = {
        'Weapons': {
            'Dagger':    {'cost': 8, 'damage': 4, 'armor': 0},
            'Shortsword': {'cost': 10, 'damage':    5,     'armor':  0},
            'Warhammer': {'cost': 25, 'damage':    6,     'armor':  0},
            'Longsword': {'cost': 40, 'damage':    7,     'armor':  0},
            'Greataxe': {'cost': 74, 'damage':    8,     'armor':  0}
        },
        'Armor': {
            'Leather':    {'cost': 13, 'damage': 0, 'armor': 1},
            'Chainmail': {'cost': 31, 'damage':    0,     'armor':  2},
            'SplintMail': {'cost': 53, 'damage':    0,     'armor':  3},
            'Bandedmail': {'cost': 75, 'damage':    0,     'armor':  4},
            'Platemail': {'cost': 102, 'damage':    0,     'armor':  5}
        },
        'Rings': {
            'damage_1':    {'cost': 25, 'damage': 1, 'armor': 0},
            'damage_2': {'cost': 50, 'damage':    2,     'armor':  0},
            'damage_3': {'cost': 100, 'damage':    3,     'armor':  0},
            'defense_1': {'cost': 20, 'damage':    0,     'armor':  1},
            'defense_2': {'cost': 40, 'damage':    0,     'armor':  2},
            'defense_3': {'cost': 80, 'damage':    0,     'armor':  3}
        }
    }

    weapons = [key for key in shop['Weapons'].keys()]
    armor = [key for key in shop['Armor'].keys()]
    rings = [key for key in shop['Rings'].keys()]

    options = weapons + armor + rings
    combos = []
    for i in range(1, len(options) + 1):
        for element in combinations(options, i):
            combos.append(list(element))

    costs = []
    for combo in combos:
        stat = {'cost': 0, 'damage': 0, 'armor': 0}
        weapon_count = 0
        armor_count = 0
        ring_count = 0
        for e in combo:
            if e in weapons and weapon_count == 0:
                stat['cost'] += shop['Weapons'][e]['cost']
                stat['damage'] += shop['Weapons'][e]['damage']
                stat['armor'] += shop['Weapons'][e]['armor']
                weapon_count += 1
            elif e in armor and armor_count == 0:
                stat['cost'] += shop['Armor'][e]['cost']
                stat['damage'] += shop['Armor'][e]['damage']
                stat['armor'] += shop['Armor'][e]['armor']
                armor_count += 1
            elif e in rings and ring_count < 2:
                stat['cost'] += shop['Rings'][e]['cost']
                stat['damage'] += shop['Rings'][e]['damage']
                stat['armor'] += shop['Rings'][e]['armor']
                ring_count += 1


        if weapon_count == 1 and battle(stat, boss):
            costs.append(stat['cost'])
    print(min(costs))


def part2():
    boss = {
        'HitPoints': 103,
        'damage': 9,
        'armor': 2
    }

    shop = {
        'Weapons': {
            'Dagger':    {'cost': 8, 'damage': 4, 'armor': 0},
            'Shortsword': {'cost': 10, 'damage':    5,     'armor':  0},
            'Warhammer': {'cost': 25, 'damage':    6,     'armor':  0},
            'Longsword': {'cost': 40, 'damage':    7,     'armor':  0},
            'Greataxe': {'cost': 74, 'damage':    8,     'armor':  0}
        },
        'Armor': {
            'Leather':    {'cost': 13, 'damage': 0, 'armor': 1},
            'Chainmail': {'cost': 31, 'damage':    0,     'armor':  2},
            'SplintMail': {'cost': 53, 'damage':    0,     'armor':  3},
            'Bandedmail': {'cost': 75, 'damage':    0,     'armor':  4},
            'Platemail': {'cost': 102, 'damage':    0,     'armor':  5}
        },
        'Rings': {
            'damage_1':    {'cost': 25, 'damage': 1, 'armor': 0},
            'damage_2': {'cost': 50, 'damage':    2,     'armor':  0},
            'damage_3': {'cost': 100, 'damage':    3,     'armor':  0},
            'defense_1': {'cost': 20, 'damage':    0,     'armor':  1},
            'defense_2': {'cost': 40, 'damage':    0,     'armor':  2},
            'defense_3': {'cost': 80, 'damage':    0,     'armor':  3}
        }
    }

    weapons = [key for key in shop['Weapons'].keys()]
    armor = [key for key in shop['Armor'].keys()]
    rings = [key for key in shop['Rings'].keys()]

    options = weapons + armor + rings
    combos = []
    for i in range(1, len(options) + 1):
        for element in combinations(options, i):
            combos.append(list(element))

    costs = []
    for combo in combos:
        stat = {'cost': 0, 'damage': 0, 'armor': 0}
        weapon_count = 0
        armor_count = 0
        ring_count = 0
        for e in combo:
            if e in weapons and weapon_count == 0:
                stat['cost'] += shop['Weapons'][e]['cost']
                stat['damage'] += shop['Weapons'][e]['damage']
                stat['armor'] += shop['Weapons'][e]['armor']
                weapon_count += 1
            elif e in armor and armor_count == 0:
                stat['cost'] += shop['Armor'][e]['cost']
                stat['damage'] += shop['Armor'][e]['damage']
                stat['armor'] += shop['Armor'][e]['armor']
                armor_count += 1
            elif e in rings and ring_count < 2:
                stat['cost'] += shop['Rings'][e]['cost']
                stat['damage'] += shop['Rings'][e]['damage']
                stat['armor'] += shop['Rings'][e]['armor']
                ring_count += 1


        if weapon_count == 1 and not battle(stat, boss):
            costs.append(stat['cost'])
    print(max(costs))

part2()