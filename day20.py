import math

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_of_factors(num, mult):
    ret = 1
    for i in range(2, int(math.sqrt(num) + 1)):
        temp_sum = 1
        term = 1
         
        while num % i == 0:
             
            num = num / i;
 
            term = term * i;
            temp_sum += term;
             
        ret = ret * temp_sum
    if num > 2:
        ret = ret * (1 + num)

    return ret * mult
 

def part1():
    target = 33100000

    found = False
    i = 1
    while not found:
        if sum_of_factors(i, 10) >= target:
            found = True
        else:
            i += 1

    print(i)

def part2():
    target = 33100000
    found = False
    i = 1
    primes = {}
    while not found:
        ret = 0
        for j in range(1, i + 1):
            if i % j == 0:
                if j in primes:
                    primes[j] = primes[j] + 1
                else:
                    primes[j] = 1
                if primes[j] - 1 < 50:
                    ret += j * 11

        if ret >= target:
            found = True
        else:
            print(i)
            i += 1


    print(i, ret)
    # 786240 33161590 

part2()
