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
    """
    begin bij laagste punten
    loop recursief door alle buurpunten
    als buurpunt niet al in basin of een 9, voeg toe
    ga dan recursief langs al zijn buurpunten
    op het einde, return het basin
    """

    basins = []
    for point in get_all_lowest_points(lines):
        basins.append(recursive(lines, point, []))

    # print(basins)
    top_3 = sorted(
        [len(basin) for basin in basins if isinstance(basin, list)], reverse=True
    )[:3]
    # print(top_3)
    return top_3[0] * top_3[1] * top_3[2]


def recursive(lines, point, basin):
    # Return when edge is reached
    if (
        point[0] == -1
        or point[0] == len(lines)
        or point[1] == -1
        or point[1] == len(lines[0])
    ):
        return None
    if point in basin or lines[point[0]][point[1]] == "9":
        return None
    basin.append(point)
    offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up down left right
    for [x_offset, y_offset] in offsets:
        neighbor = (point[0] + x_offset, point[1] + y_offset)
        # print(point, neighbor)
        recursive(lines, neighbor, basin)

    return basin


def get_all_lowest_points(lines):
    row_idx = col_idx = 0
    while row_idx < len(lines):
        while col_idx < len(lines[row_idx]):
            lowest_point = get_next_lowest_point(lines, row_idx, col_idx)
            if lowest_point == None:
                return
            row_idx = lowest_point[0]
            col_idx = lowest_point[1] + 1
            if col_idx >= 100:
                col_idx = 0
                row_idx += 1
            yield lowest_point


def get_next_lowest_point(lines, row_idx, col_idx):
    # print("Call function with params: ", row_idx, col_idx)
    for i in range(row_idx, len(lines)):
        for j in range(col_idx, len(lines[i])):
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

            return (i, j)

        col_idx = 0  # reset col_idx if no result is found on current line


def main():
    lines = read_file()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
