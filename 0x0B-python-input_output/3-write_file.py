#!/usr/bin/python3
def write_file(filename="", text=""):
    """ writes a string UTF8 to a text file
    returns the number of characters written
    filename: name of the file.
    text: the text to insert
    """

    with open(filename, 'w') as f:
        n = f.write(text)
        f.close()
        return n
