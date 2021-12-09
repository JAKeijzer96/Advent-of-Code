import string


def read_file():
    lines = []
    with open("../resources/day4.txt") as file:
        lines = file.read().splitlines()

    return lines


def filter_lines(lines):
    filtered_lines = []
    filtered_line = ""
    for line in lines:
        if line:
            filtered_line += line + " "
        else:
            filtered_lines.append(filtered_line[: len(filtered_line) - 1])
            filtered_line = ""

    filtered_lines.append(
        filtered_line[: len(filtered_line) - 1]
    )  # f&^*king off by one error
    return filtered_lines


def part1(lines):
    required_passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for line in lines:
        passport_keys = [
            key for key, value in [split_line.split(":") for split_line in line.split()]
        ]
        if all(key in passport_keys for key in required_passport_fields):
            valid_passports += 1

    return valid_passports


def part2(lines):
    nr_of_valid_passports = 0

    for line in lines:
        split_passport = [
            [key, value]
            for key, value in [split_line.split(":") for split_line in line.split()]
        ]

        passport_dict = dict()
        for key, value in split_passport:
            passport_dict[key] = value

        if is_valid_passport(passport_dict):
            nr_of_valid_passports += 1

    return nr_of_valid_passports


def is_valid_passport(passport_dict):
    byr = passport_dict.get("byr")
    iyr = passport_dict.get("iyr")
    eyr = passport_dict.get("eyr")
    hgt = passport_dict.get("hgt")
    hcl = passport_dict.get("hcl")
    ecl = passport_dict.get("ecl")
    pid = passport_dict.get("pid")
    # Hurrah for readability! :^)
    return (
        byr and 1920 <= int(byr) <= 2002
        and iyr and 2010 <= int(iyr) <= 2020
        and eyr and 2020 <= int(eyr) <= 2030
        and hgt and
            ((hgt.endswith("cm") and 150 <= int(hgt[: len(hgt) - 2]) <= 193)
            or (hgt.endswith("in") and 59 <= int(hgt[: len(hgt) - 2]) <= 76))
        and hcl and (hcl.startswith("#") and all(char in string.hexdigits for char in hcl[1:]))
        and ecl and (ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        and pid and (len(pid) == 9) and all(char in string.digits for char in pid))


def main():
    lines = read_file()
    filtered_lines = filter_lines(lines)
    print(part1(filtered_lines))
    print(part2(filtered_lines))


if __name__ == "__main__":
    main()
