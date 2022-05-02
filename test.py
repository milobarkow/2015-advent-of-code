from itertools import combinations
def print_powerset(string):
    ret = []
    for i in range(0,len(string)+1):
        for element in combinations(string,i):
            ret.append(element)
    return ret
string=['a','b','c']
