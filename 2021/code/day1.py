def count_increases():

    lines = []
    with open("../resources/day1input.txt") as file:
        lines = file.readlines()

    increases = 0
    previous_depth = int(lines[0])
    for line in lines[1:]:
        current_depth = int(line)
        if current_depth > previous_depth:
            increases += 1
        previous_depth = current_depth
    print(increases)


def count_triple_increases():

    lines = []
    with open("../resources/day1input.txt") as file:
        lines = file.readlines()

    increases = 0
    previous_depth = int(lines[0]) + int(lines[1]) + int(lines[2])
    for idx in range(1, len(lines) - 2):
        current_depth = int(lines[idx]) + int(lines[idx + 1]) + int(lines[idx + 2])
        if current_depth > previous_depth:
            increases += 1
        previous_depth = current_depth
    print(increases)


def main():
    count_triple_increases()


if __name__ == "__main__":
    main()
