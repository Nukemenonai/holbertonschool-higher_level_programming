#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
    curr = 0
    lttr = roman_string[curr]
    total = 0
    if not roman_string:
        return 0
    else:
        for lttr in roman_string:
            if lttr not in romans:
                return 0
            else:
                if curr == 0:
                    total = romans[lttr]
                    curr += 1
                else:
                    if romans[lttr] <= romans[roman_string[curr - 1]]:
                        total = romans[lttr] + total
                        curr += 1
                    elif romans[lttr] > romans[roman_string[curr - 1]]:
                        total = romans[lttr] - total
                        curr += 1
        return total
