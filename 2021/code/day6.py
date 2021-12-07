def read_file():
    lines = []
    with open("../resources/day6input.txt") as file:
        lines = file.readlines()

    first_line = [int(x) for x in lines[0].rstrip("\n").split(",")]
    return first_line


def make_dict():
    _list = read_file()
    fish_dict = dict()
    for nr in range(9):
        fish_dict[nr] = 0
    
    for nr in _list:
        fish_dict[nr] += 1

    return fish_dict


def loop_over_dict(fish_dict):
    # Take value of key 0 and save to a temp var
    # Then loop through dict, moving each value down 1 key.
    # After looping use previous value of key 0 to add to fish at 6 and add new fish at 8
    for _ in range(256):
        fish_at_zero = fish_dict[0]
        for nr in range(1, 9):
            fish_dict[nr - 1] = fish_dict[nr]
        fish_dict[6] += fish_at_zero
        fish_dict[8] = fish_at_zero
    
    total_count = 0
    for nr in range(0, 9):
        total_count += fish_dict[nr]

    print(total_count)


def main():
    fish_dict = make_dict()
    loop_over_dict(fish_dict)
    # _list = read_file()
    # for _ in range(80):
    #     length = len(_list)
    #     for idx in range(length):
    #         if _list[idx] == 0:
    #             _list[idx] = 6
    #             _list.append(8)
    #         else:
    #             _list[idx] -= 1

    # print(len(_list))


if __name__ == "__main__":
    main()
