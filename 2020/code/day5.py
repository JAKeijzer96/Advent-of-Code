def read_file():
    lines = []
    with open("../resources/day5.txt") as file:
        lines = file.read().splitlines()

    return lines

def part1(lines):
    max_seat_id = 0
    for line in lines:
        seat_id = get_seat_id(line)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    
    return max_seat_id

def get_seat_id(line):
    min_row = 0
    max_row = 127
    half = 64
    for char in line[:7]:
        if char == 'F':
            max_row -= half
        elif char == 'B':
            min_row += half
        half //= 2
    
    min_col = 0
    max_col = 7
    half = 4
    for char in line[7:]:
        if char == 'L':
            max_col -= half
        elif char == 'R':
            min_col += half
        half //= 2
    
    return min_row * 8 + min_col

def part2(lines):
    seat_ids = []
    for line in lines:
        seat_ids.append(get_seat_id(line))
    
    seat_ids = sorted(seat_ids)
    for idx in range(len(seat_ids)):
        if seat_ids[idx] + 1 != seat_ids[idx + 1]:
            return seat_ids[idx] + 1

def main():
    lines = read_file()
    print(part1(lines))
    print(part2(lines))

if __name__ == "__main__":
    main()