#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(0, l):
        char = str[i]
        if i != (len(str) - 1):
            if ord(char) >= 97 and ord(char) <= 122:
                char = chr(ord(char) - 32)
            print("{}".format(char), end="")
        else:
            if ord(char) >= 97 and ord(char) <= 122:
                char = chr(ord(char) - 32)
            print("{}".format(char))
