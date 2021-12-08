def read_file():
    lines = []
    with open("../resources/day8input.txt") as file:
        lines = file.read().splitlines()

    for idx in range(len(lines)):
        lines[idx] = lines[idx].split(" | ")
        lines[idx][0] = lines[idx][0].split()
        lines[idx][1] = lines[idx][1].split()

    return lines


def part1(lines):
    counter = 0
    for splitline in lines:
        for word in splitline[1]:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                counter += 1
    return counter


def part2(splitlines) -> int:
    """
     aaaa    In elke splitline staan 2 lists, de eerste list bevat 10 'input' strings
    b    c   en de tweede list bevat 4 'output' strings.
    b    c   Om uit te vogelen welke letter voor welk getal staat moeten we eerst uitvinden
     dddd    welke letter welk deel van de 7-digit display aan- of uitzet.
    e    f   Stap 1 hiervoor is bepalen welke woorden lengte 2, 3, 4 of 7 hebben.
    e    f   Woord met lengte 2 is het getal 1, lengte 3: getal 7, lengte 4: getal 4, lengte 7: getal 8
     gggg

    Het woord van lengte 5 dat beide letters bevat van het getal 1 is het getal 3
    Het woord van lengte 6 dat alle letters bevat van het getal 3 is het getal 9
    
    Van de resterende woorden van lengte 5 is het woord dat het karakter bevat dat wel in 9 zit maar niet in 3 het getal 5
    Het laatste woord van lengte 5 is het getal 2

    De letter die wel voorkomt in het getal 4 en niet in het getal 5 is de rechter boven verticale bar
    Van de resterende woorden van lengte 6 is het woord dat deze letter bevat het getal 0
    Het laatste woord van lengte 6 is het getal 6

    Omdat de volgorde van de letters van de 'input' en de 'output' niet hetzelfde zijn wordt er nog gesorteerd
    """

    total_sum = 0
    for splitline in splitlines:
        result_dict = analyze_splitline(splitline[0])
        result_str = ""
        for word in splitline[1]:
            word = "".join(sorted(word))
            result_str += result_dict[word]

        total_sum += int(result_str)
    return total_sum


def analyze_splitline(word_list):
    result_list = ['' for x in range(10)]
    words_of_length_5 = []
    words_of_length_6 = []
    for word in word_list:
        if len(word) == 2:
            result_list[1] = "".join(sorted(word))
        elif len(word) == 3:
            result_list[7] = "".join(sorted(word))
        elif len(word) == 4:
            result_list[4] = "".join(sorted(word))
        elif len(word) == 5:
            words_of_length_5.append(word)
        elif len(word) == 6:
            words_of_length_6.append(word)
        elif len(word) == 7:
            result_list[8] = "".join(sorted(word))

    for word in words_of_length_5:
        if all(letter in word for letter in result_list[1]):
            result_list[3] = "".join(sorted(word))
            words_of_length_5.remove(word)
            break

    for word in words_of_length_6:
        if all(letter in word for letter in result_list[3]):
            result_list[9] = "".join(sorted(word))
            words_of_length_6.remove(word)
            break

    # Extra karakter in 9 vergeleken met 3 vinden, hiermee 2 en 5 bepalen
    for char in result_list[9]:
        if char not in result_list[3]:
            top_left_vert_bar = char
            for word in words_of_length_5:
                if top_left_vert_bar in word:
                    result_list[5] = "".join(sorted(word))
                    words_of_length_5.remove(word)
                    result_list[2] = "".join(sorted(words_of_length_5[0])) # resterende getal is 2
                    del words_of_length_5
    
    
    for char in result_list[4]:
        if char not in result_list[5]:
            top_right_vert_bar = char
            for word in words_of_length_6:
                if top_right_vert_bar in word:
                    result_list[0] = "".join(sorted(word))
                    words_of_length_6.remove(word)
                    result_list[6] = "".join(sorted(words_of_length_6[0])) # resterende getal is 6
                    del words_of_length_6
    
    result_dict = {key: str(value) for value, key in enumerate(result_list)}
    return result_dict


def main():
    splitlines = read_file()
    # print(part1(splitlines))
    print(part2(splitlines))


if __name__ == "__main__":
    main()


"""
basisapp zo ruw mogelijk iig staat die aan andere websites de mogelijkheid geeft om verificatie te doen
een vorm van leeftijdsverificatie en locatieverificatie

als azure ad/oauth verwisselbaar maken, dan prima

als op beeldende manier kunnen laten zien dat het werkt is het nice
webadmin van website gemakkelijk onze tool kan implementeren

"""
