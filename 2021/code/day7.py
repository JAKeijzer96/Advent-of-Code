def read_file():
    lines = []
    with open("../resources/day7input.txt") as file:
        lines = file.readlines()
    
    first_line = [int(x) for x in lines[0].rstrip("\n").split(",")]
    return first_line

def part1(_list):
    minimum = min(_list)
    maximum = max(_list)
    res = dict()

    for i in range(minimum, maximum):
        total_fuel_cost = 0
        for nr in _list:
            total_fuel_cost += abs(nr - i)
        res[i] = total_fuel_cost
        total_fuel_cost = 0
    
    horizontal_pos = min(res, key=res.get)
    return res[horizontal_pos]

def part2(_list):
    minimum = min(_list)
    maximum = max(_list)
    res = dict()

    for i in range(minimum, maximum):
        total_fuel_cost = 0
        for nr in _list:
            total_fuel_cost += (0.5 * abs(nr - i) * (abs(nr - i) + 1))
        res[i] = total_fuel_cost
        total_fuel_cost = 0
    
    horizontal_pos = min(res, key=res.get)
    return res[horizontal_pos]

def main():
    firstline = read_file()
    print(part2(firstline))

if __name__ == '__main__':
    main()