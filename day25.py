def generate_next_code(num):
    return (num * 252533) % 33554393



def part1():
    end_row, end_column = 3010 - 1, 3019 - 1
    start, last_num = 20151125, 20151125
    i, j, tracker = 0, 0, 0
    found = False
    while not found:
        while i >= 0 and not found:
            if i == 0 and j == 0:
                pass
            else:
                last_num = generate_next_code(last_num)
                if i == end_row and j == end_column:
                    found = True
            i -= 1
            j += 1
        tracker += 1
        i = tracker
        j = 0
    print(last_num)


    


part1()


#  1 3 6 10 15
#  2 5 9 14
#  4 8 13
#  7 12
#  11


