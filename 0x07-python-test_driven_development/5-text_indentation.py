#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after any of these chars:
       . ? :
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    new_str = text.replace(': ', ':\n\n')
    new_str = new_str.replace('. ', '.\n\n')
    new_str = new_str.replace('? ', '?\n\n')
    print(new_str)
