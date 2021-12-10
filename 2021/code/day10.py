def read_file():
    lines = []
    with open("../resources/day10input.txt") as file:
        lines = file.read().splitlines()

    return lines


open_char_dict = {"<": ">", "(": ")", "[": "]", "{": "}"}
close_char_dict = {">": "<", ")": "(", "]": "[", "}": "{"}
score_dict_part_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_dict_part_2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def part1(lines):
    total_sum = 0
    for line in lines:
        total_sum += with_stack_part_1(line)

    return total_sum


def with_stack_part_1(line):
    stack = []
    for char in line:
        if char in open_char_dict:
            stack.append(char)

        elif char in close_char_dict:
            last_char = stack.pop()
            if last_char != close_char_dict[char]:
                return score_dict_part_1[char]

    return 0


def part2(lines):
    filtered_lines = []
    for filtered_line in lines:
        if not with_stack_part_1(filtered_line):
            filtered_lines.append(filtered_line)

    result_list = []
    for filtered_line in filtered_lines:
        result_list.append(with_stack_part_2(filtered_line))

    result_list.sort()
    return result_list[len(result_list) // 2]


def with_stack_part_2(line):
    stack = []
    for char in line:
        if char in open_char_dict:
            stack.append(char)
        elif char in close_char_dict:
            last_char = stack.pop()

    result = 0
    while len(stack) > 0:
        char = stack.pop()
        result = result * 5 + score_dict_part_2[char]

    return result


def main():
    lines = read_file()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
