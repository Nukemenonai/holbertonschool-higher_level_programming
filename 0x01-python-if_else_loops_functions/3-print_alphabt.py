#!/usr/bin/python3
x = 97
for i in range(97, 123):
    if chr(x) == "q" or chr(x) == "e":
        x = x + 1
        continue

    print("{}".format(chr(x)), end="")
    x = x + 1
