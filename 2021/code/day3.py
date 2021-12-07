def calc_power_consumption():
    lines = []
    with open("../resources/day3input.txt") as file:
        lines = file.readlines()

    for line in lines:
        line.split()

    inverted_lines = [list(x) for x in zip(*lines)]
    # print(inverted_lines)
    gamma_rate = ""
    epsilon_rate = ""
    for tup in inverted_lines[: len(inverted_lines) - 1]:
        zeroes = tup.count("0")
        ones = tup.count("1")
        gamma_rate += "0" if (zeroes > ones) else "1"
        epsilon_rate += "1" if (zeroes > ones) else "0"

    gamma_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    return gamma_rate_dec * epsilon_rate_dec


def calc_life_support(most_common = True):
    lines = []
    with open("../resources/day3input.txt") as file:
        lines = file.readlines()
    for idx in range(len(lines)):
        lines[idx] = lines[idx].rstrip("\n")

    starting_value = ""
    for idx in range(len(lines[0])):
        zeroes = 0
        ones = 0
        
        for line in lines:
            if line[idx] == "0":
                zeroes += 1
            elif line[idx] == "1":
                ones += 1
        if (most_common):
            starting_value += "1" if (ones >= zeroes) else "0"
        else:
            starting_value += "1" if (zeroes > ones) else "0"
        lines_copy = [ln for ln in lines if ln.startswith(starting_value)]
        lines = lines_copy
        if len(lines) == 1:
            # print(lines[0])
            return(int(lines[0],2))


def main():
    print(calc_power_consumption())
    print(calc_life_support() * calc_life_support(most_common=False))


if __name__ == "__main__":
    main()
