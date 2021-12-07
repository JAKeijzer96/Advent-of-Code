lines_list = []
board = [["." for i in range(1000)] for j in range(1000)]


def read_file():
    lines = []
    with open("./resources/day5input.txt") as file:
        lines = file.readlines()

    for idx in range(len(lines)):
        lines[idx] = lines[idx].rstrip("\n").split(" -> ")

    global lines_list
    lines_list = lines


def draw_line(line):
    starting_point = [int(x) for x in line[0].split(",")]
    end_point = [int(x) for x in line[1].split(",")]
    print(starting_point, end_point)

    # For part 1: Return if the line is not vertical or horizontal
    # if starting_point[0] != end_point[0] and starting_point[1] != end_point[1]:
    #     return

    # vertical
    if starting_point[0] == end_point[0]:
        if starting_point[1] < end_point[1]:
            while starting_point[1] <= end_point[1]:
                increment(starting_point[0], starting_point[1])
                starting_point[1] += 1
        else:
            while starting_point[1] >= end_point[1]:
                increment(starting_point[0], starting_point[1])
                starting_point[1] -= 1
    # horizontal
    elif starting_point[1] == end_point[1]:
        print(starting_point, end_point)
        if starting_point[0] < end_point[0]:
            while starting_point[0] <= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] += 1
        else:
            while starting_point[0] >= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] -= 1
    # diagonal
    else:
        # left to right, up
        if starting_point[0] < end_point[0] and starting_point[1] < end_point[1]:
            while starting_point[0] <= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] += 1
                starting_point[1] += 1
        # left to right, down
        elif starting_point[0] < end_point[0] and starting_point[1] > end_point[1]:
            while starting_point[0] <= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] += 1
                starting_point[1] -= 1
        # right to left, up
        elif starting_point[0] > end_point[0] and starting_point[1] < end_point[1]:
            while starting_point[0] >= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] -= 1
                starting_point[1] += 1
        # right to left, down
        elif starting_point[0] > end_point[0] and starting_point[1] > end_point[1]:
            while starting_point[0] >= end_point[0]:
                increment(starting_point[0], starting_point[1])
                starting_point[0] -= 1
                starting_point[1] -= 1


def increment(i, j):
    if board[i][j] == ".":
        board[i][j] = 1
    else:
        board[i][j] += 1


def main():
    read_file()
    for line in lines_list:
        draw_line(line)
    total_count = 0
    for row in board:
        for nr in row:
            if isinstance(nr, int) and nr >= 2:
                total_count += 1
    print(total_count)


if __name__ == "__main__":
    main()
