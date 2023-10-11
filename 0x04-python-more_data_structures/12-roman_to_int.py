#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    maxlist = max(list_num)

    for n in list_num:
        if maxlist > n:
            sub += n

    return (maxlist - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listkeys = list(rom.keys())

    num = 0
    lastrom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in listkeys:
            if r_num == ch:
                if rom.get(ch) <= lastrom:
                    num += to_subtract(list_num)
                    list_num = [rom.get(ch)]
                else:
                    list_num.append(rom.get(ch))

                lastrom = rom.get(ch)

    num += to_subtract(list_num)

    return (num)
