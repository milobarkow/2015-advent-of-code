import itertools

def part1():
    with open('input.txt') as file:
        data = [line.strip().split(' ') for line in file]

    checkVisit = {}
    names = []
    trip = []
    allTrips = []
    i = 0

    for line in data:
        a = line[0]
        b = line[2]
        if a not in checkVisit:
            checkVisit[a] = -1
            names.append(a)
        if b not in checkVisit:
            checkVisit[b] = -1
            names.append(b)

    trip.append(names[i])
    checkVisit[trip[i]] = 1

    count = 0
    done = False
    while not done:
        minDist = 1000
        nextCountry = ''
        for line in data:
            travelingFrom = trip[-1]
            if line[0] == travelingFrom or line[2] == travelingFrom:
                if line[0] == travelingFrom and checkVisit[line[2]] == -1:
                    if int(line[-1]) < minDist:
                        minDist = int(line[-1])
                        nextCountry = line[2]
                elif checkVisit[line[0]] == -1:
                    if int(line[-1]) < minDist:
                        minDist = int(line[-1])
                        nextCountry = line[0]

        count += minDist
        trip.append(nextCountry)
        checkVisit[nextCountry] = 1

        if len(trip) >= len(checkVisit):
            allTrips.append(count)
            if len(allTrips) >= len(trip):
                done = True
            else:
                i += 1
                trip = []
                count = 0
                for key in checkVisit:
                    checkVisit[key] = -1

                trip.append(names[i])
                checkVisit[trip[0]] = 1

    print(min(allTrips))


def part2():
    with open('input.txt') as file:
        data = [line.strip().split(' ') for line in file]

    checkVisit = {}
    names = []

    for line in data:
        a = line[0]
        b = line[2]
        if a not in checkVisit:
            checkVisit[a] = -1
            names.append(a)
        if b not in checkVisit:
            checkVisit[b] = -1
            names.append(b)

    trips = list(itertools.permutations(names))
    distances = []

    for trip in trips:
        distance = 0
        for i in range(len(names) - 1):
            for line in data:
                if trip[i] in line and trip[i + 1] in line:
                    distance += int(line[-1])
                    break

        distances.append(distance)

    print(max(distances))



part2()
