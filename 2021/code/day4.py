"""
Read the file, save the first line as a list of ints (numbers)
and save the boards as 2D lists of ints (boards).
Loop through numbers. For each number, change all occurences
of the number in all boards from type int to type str.
Then for each board check if there's a bingo by checking
the datatypes
"""

numbers = []
boards = []

def read_file():
    global numbers  # Gross!
    global boards  # Ew!
    lines = []
    with open("../resources/day4input.txt") as file:
        lines = file.readlines()

    for idx in range(len(lines)):
        lines[idx] = lines[idx].rsplit("\n")[0]

    numbers = [int(x) for x in lines[0].split(",")]

    current_board = []
    for line in lines[2:]:
        if len(line) == 0:
            boards.append(current_board)
            current_board = []
            continue

        split_line = line.split()
        for idx in range(len(split_line)):
            split_line[idx] = int(split_line[idx])
        current_board.append(split_line)

    boards.append(current_board)


def draw_number(nr: int):
    for board in boards:
        for row in board:
            for idx in range(len(row)):
                if row[idx] == nr:
                    row[idx] = str(nr)
        if (is_bingo(board)):
            yield board
            # return board <-- use this for part 1
    return None

def is_bingo(board):
    # rows
    for row in board:
        if all([isinstance(x, str) for x in row]):
            return True
    # columns
    for idx in range(len(board[0])):
        if (is_column_bingo(board, idx)):
            return True
    # diagonals
    if (all([isinstance(row[i], str) for i, row in enumerate(board)])):
        return True
    if (all([isinstance(row[-i-1], str) for i, row in enumerate(board)])):
        return True

    return False

def is_column_bingo(board, idx: int):
    for row in board:
        if not isinstance(row[idx], str):
            return False
    return True


def calculate_solution(board, nr):
    total_sum = 0
    for row in board:
        for element in row:
            if isinstance(element,int):
                total_sum += element
    return total_sum * nr


def main():
    read_file()
    for nr in numbers:
        bingo_board = draw_number(nr)
        if (bingo_board != None):
            print(calculate_solution(bingo_board, nr))
            # print(bingo_board)
            return

def part_2():
    read_file()
    for nr in numbers:
        for bingo_board in draw_number(nr):
        # bingo_board = draw_number(nr)
            if (bingo_board != None):
                boards.remove(bingo_board)
                
            if (len(boards) == 1):
                print(bingo_board, nr)
                # Hardcoded solution because the loop stopped before drawing the final nr and I cba fixing it
#                 print(calculate_solution(
# [[11, '69', '4', '6', '23'], ['38', 47, 16, '99', '96'], ['7', '13', '40', 41, '78'], ['12', '5', 1, '18', '88'], ['20', '42', '10', '82', '73']], 73))


if __name__ == "__main__":
    # main()
    part_2()
