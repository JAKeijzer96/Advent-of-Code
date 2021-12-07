def navigate():
    lines = []
    with open("../resources/day2input.txt") as file:
        lines = file.readlines()

    forward = 0
    depth = 0
    for line in lines:
        if line.startswith("forward"):
            forward += int(line.split(" ")[1])
        elif line.startswith("down"):
            depth += int(line.split(" ")[1])
        elif line.startswith("up"):
            depth -= int(line.split(" ")[1])
    print(depth * forward)


def navigate_v2():
    lines = []
    with open("../resources/day2input.txt") as file:
        lines = file.readlines()

    forward = 0
    depth = 0
    aim = 0
    for line in lines:
        if line.startswith("forward"):
            forward += int(line.split(" ")[1])
            depth += int(line.split(" ")[1]) * aim
        elif line.startswith("down"):
            aim += int(line.split(" ")[1])
        elif line.startswith("up"):
            aim -= int(line.split(" ")[1])
    print(depth * forward)


def main():
    navigate_v2()


if __name__ == "__main__":
    main()
