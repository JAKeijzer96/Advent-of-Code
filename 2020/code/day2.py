def read_file():
    lines = []
    with open("../resources/day2.txt") as file:
        lines = file.read().splitlines()
    return lines


def is_single_line_valid_part_1(line):
    split_line = line.split(" ")
    min_occurences = int(split_line[0].split("-")[0])
    max_occurences = int(split_line[0].split("-")[1])
    letter = split_line[1][0]
    password = split_line[2]
    return min_occurences <= password.count(letter) <= max_occurences


def is_single_line_valid_part_2(line):
    split_line = line.split(" ")
    idx_1 = int(split_line[0].split("-")[0]) - 1
    idx_2 = int(split_line[0].split("-")[1]) - 1
    letter = split_line[1][0]
    password = split_line[2]
    if ( (password[idx_1] == letter and password[idx_2] != letter)
        or (password[idx_1] != letter and password[idx_2] == letter) ):
        return True
    return False


def main():
    lines = read_file()
    valid_count = 0
    for line in lines:
        if is_single_line_valid_part_2(line):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    main()
