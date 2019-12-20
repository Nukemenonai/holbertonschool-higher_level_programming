#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    #if len(roman_string) == 0:
        #return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    curr = 0
    lttr = roman_string[curr]
    total = 0
    ocurr = 1

    for lttr in roman_string:
        if lttr not in romans:
            return 0
        if curr == 0:
            total = romans[lttr]
            curr += 1
        else:
            if romans[lttr] < romans[roman_string[curr - 1]]:
                ocurr = 1
                total = romans[lttr] + total
                curr += 1
            elif romans[lttr] > romans[roman_string[curr - 1]]:
                ocurr = 1
                total += romans[lttr]
                total -= (2 * romans[roman_string[curr - 1]])
                curr += 1
            elif romans[lttr] == romans[roman_string[curr - 1]]:
                total = romans[lttr] + total
                curr += 1
                ocurr += 1
                if ocurr >= 4:
                    return 0
    return total
