#!/usr/bin/python3
def multiple_returns(sentence):
    character = ""
    length = 0
    if not sentence:
        character = None
    else:
        character = sentence[0]
        length = len(sentence)

    return length, character
