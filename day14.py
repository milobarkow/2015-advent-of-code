def part1():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]

    deers = [{
        'speed': int(line[3]),
        'time': int(line[6]),
        'rest': int(line[-2]),
        'distance': 0,
        'currentRest': 0,
        'currentFly': 0,
        'flying': True
    } for line in data]

    for i in range(2503):
        for deer in deers:
            if deer['flying']:
                if deer['currentFly'] < deer['time']:
                    deer['distance'] += deer['speed']
                    deer['currentFly'] += 1
                elif deer['currentFly'] == deer['time']:
                    deer['currentFly'] = 0
                    deer['currentRest'] += 1
                    deer['flying'] = False
            else:
                if deer['currentRest'] < deer['rest']:
                    deer['currentRest'] += 1
                elif deer['currentRest'] == deer['rest']:
                    deer['currentRest'] = 0
                    deer['currentFly'] += 1
                    deer['distance'] += deer['speed']
                    deer['flying'] = True
    distances = [deer['distance'] for deer in deers]


def part2():
    with open('input.txt') as file:
        data = [line.strip().split() for line in file]

    deers = [{
        'speed': int(line[3]),
        'time': int(line[6]),
        'rest': int(line[-2]),
        'distance': 0,
        'currentRest': 0,
        'currentFly': 0,
        'flying': True,
        'points': 0
    } for line in data]

    for i in range(2503):
        for deer in deers:
            if deer['flying']:
                if deer['currentFly'] < deer['time']:
                    deer['distance'] += deer['speed']
                    deer['currentFly'] += 1
                elif deer['currentFly'] == deer['time']:
                    deer['currentFly'] = 0
                    deer['currentRest'] += 1
                    deer['flying'] = False
            else:
                if deer['currentRest'] < deer['rest']:
                    deer['currentRest'] += 1
                elif deer['currentRest'] == deer['rest']:
                    deer['currentRest'] = 0
                    deer['currentFly'] += 1
                    deer['distance'] += deer['speed']
                    deer['flying'] = True

        maxDistance = max([deer['distance'] for deer in deers])

        for deer in deers:
            if deer['distance'] == maxDistance:
                deer['points'] += 1

    points = [deer['points'] for deer in deers]
    print(max(points))

