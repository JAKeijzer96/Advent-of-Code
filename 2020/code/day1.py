def read_file():
    lines = []
    with open("../resources/day1.txt") as file:
        lines = file.readlines()

    for idx in range(len(lines)):
        lines[idx] = lines[idx].rstrip("\n")
    
    return [int(line) for line in lines]


def main():
    _list = read_file()
    for i in range(len(_list)):
        for j in range(i, len(_list)):
            for k in range(j, len(_list)):
                if (_list[i] + _list[j] + _list[k] == 2020):
                    print(_list[i], _list[j], _list[k], _list[i] * _list[j] * _list[k])
                    return
    


if __name__ == "__main__":
    main()