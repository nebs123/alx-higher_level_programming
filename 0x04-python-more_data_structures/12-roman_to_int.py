#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    numeral = 0
    count = 0
    prev = ""
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(roman_string)):
        if roman_string[i] in romans:
            if roman_string[i] == prev and count == 3:
                return 0

            if roman_string[i] == prev:
                count += 1
            else:
                count = 1
                prev = roman_string[i]

            if i < (len(roman_string) - 1) and romans[roman_string[i]]\
               < romans[roman_string[i + 1]]:
                if count >= 2 or roman_string[i + 2: i + 3] == roman_string[i]:
                    return 0
                if (romans[roman_string[i + 1]] - romans[roman_string[i]])\
                   in [4, 9, 40, 90, 400, 900]:
                    numeral -= romans[roman_string[i]]
                else:
                    return 0
            else:
                numeral += romans[roman_string[i]]
        else:
            return 0
    return numeral
