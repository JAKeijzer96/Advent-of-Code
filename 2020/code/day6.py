def read_file():
    lines = []
    with open("../resources/day6.txt") as file:
        lines = file.read().splitlines()

    return lines


def filter_lines_part_1(lines):
    filtered_lines = []
    filtered_line = ""
    for line in lines:
        if len(line) == 0:
            filtered_lines.append(filtered_line)
            filtered_line = ""
        else:
            filtered_line += line
    filtered_lines.append(filtered_line)
    return filtered_lines


def filter_lines_part_2(lines):
    filtered_lines = []
    filtered_line = ""
    for line in lines:
        if len(line) == 0:
            filtered_lines.append(filtered_line[: len(filtered_line) - 1])
            filtered_line = ""
        else:
            filtered_line += line + ","
    filtered_lines.append(filtered_line[: len(filtered_line) - 1])
    return filtered_lines


def part1(filtered_lines):
    count = 0
    for line in filtered_lines:
        count += len(set(line))
    return count


def part2(filtered_lines):
    # Take the first answer of a groupe as base, then check if
    # its characters are present in the other answers
    count = 0
    for line in filtered_lines:
        split_line = line.split(",")
        first_answer = split_line[0]

        for other_answer in split_line[1:]:
            for char in first_answer:
                if not char in other_answer:
                    first_answer = first_answer.replace(char, "")

        # print(split_line, x)
        count += len(first_answer)

    return count


def main():
    lines = read_file()
    filtered_lines_part_1 = filter_lines_part_1(lines)
    print(part1(filtered_lines_part_1))
    filtered_lines_part_2 = filter_lines_part_2(lines)
    print(part2(filtered_lines_part_2))


if __name__ == "__main__":
    main()
