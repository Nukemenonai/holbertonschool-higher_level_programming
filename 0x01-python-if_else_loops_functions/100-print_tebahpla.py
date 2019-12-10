#!/usr/bin/python3
for number in range(122, 96, -1):
    if number % 2 != 0:
        number -= 32
    print("{}".format(chr(number)), end="")
