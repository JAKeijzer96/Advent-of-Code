def read_file():
    lines = []
    with open("../resources/day3.txt") as file:
        lines = file.read().splitlines()
    return lines


def move_to_bottom(lines, right=3, down=1):
    line_length = len(lines[0])
    current_pos = 0
    nr_of_trees = 0
    for idx, line in enumerate(lines):
        if not (idx % down):
            if line[current_pos] == "#":
                nr_of_trees += 1
            current_pos += right
            if current_pos >= line_length:
                current_pos %= line_length

    return nr_of_trees


def part1():
    lines = read_file()
    print(move_to_bottom(lines))


def part2():
    lines = read_file()
    total_nr_of_trees = 1
    total_nr_of_trees *= move_to_bottom(lines, right=1)
    total_nr_of_trees *= move_to_bottom(lines, right=3)
    total_nr_of_trees *= move_to_bottom(lines, right=5)
    total_nr_of_trees *= move_to_bottom(lines, right=7)
    total_nr_of_trees *= move_to_bottom(lines, right=1, down=2)
    print(total_nr_of_trees)

def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
