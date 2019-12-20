#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
              'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'MC': 900, 'M': 1000}
    curr = 0
    lttr = roman_string[curr]
    total = 0
    ocurr = 1
    if roman_string is None:
        return 0
    elif type(roman_string) is not str:
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
                    if romans[lttr] < romans[roman_string[curr - 1]]:
                        ocurr = 1
                        total = romans[lttr] + total
                        curr += 1
                    elif romans[lttr] > romans[roman_string[curr - 1]]:
                        ocurr = 1
                        compound = roman_string[curr - 1] + roman_string[curr]
                        if compound in romans:
                            total -= romans[roman_string[curr - 1]]
                            total += romans[compound]
                            curr += 2
                            continue
                        else:
                            return 0
                            # total = romans[lttr] - total
                            # curr += 1
                    elif romans[lttr] == romans[roman_string[curr - 1]]:
                        total = romans[lttr] + total
                        curr += 1
                        ocurr += 1
                        if ocurr >= 4:
                            return 0
        return total
