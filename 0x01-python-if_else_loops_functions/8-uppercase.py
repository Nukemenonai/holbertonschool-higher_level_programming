#!/usr/bin/python3
def uppercase(str):
    res = ''
    for char in str:
        char = ord(char)
        if char >= 97 and char <= 122:
            res += chr(char - 32)
        elif char >= 65 and char <= 90:
            res += chr(char)
        else:
            res += chr(char)
    print("{}".format(res))
