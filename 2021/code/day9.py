def read_file():
    lines = []
    with open("../resources/day9input.txt") as file:
        lines = file.read().splitlines()

    return lines


def part1(lines):
    risk_lvl_sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i == 0:
                # only check down
                if not (lines[i][j] < lines[i + 1][j]):
                    continue
            elif i == len(lines) - 1:
                # only check up
                if not (lines[i][j] < lines[i - 1][j]):
                    continue
            else:
                # check up and down
                if not (
                    lines[i][j] < lines[i - 1][j] and lines[i][j] < lines[i + 1][j]
                ):
                    continue

            if j == 0:
                # only check right
                if not (lines[i][j] < lines[i][j + 1]):
                    continue
            elif j == len(lines[i]) - 1:
                # only check left
                if not (lines[i][j] < lines[i][j - 1]):
                    continue
            else:
                # check left and right
                if not (
                    lines[i][j] < lines[i][j - 1] and lines[i][j] < lines[i][j + 1]
                ):
                    continue

            risk_lvl = int(lines[i][j]) + 1
            risk_lvl_sum += risk_lvl

    return risk_lvl_sum


def part2(lines):

    pass


def main():
    lines = read_file()
    print(part1(lines))


if __name__ == "__main__":
    main()
