#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after any of these chars:
       . ? :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ['.','?',':']:
            text = text[:(i + 1)] + '\n' + '\n' + text[(i + 2):]
    print(text)
