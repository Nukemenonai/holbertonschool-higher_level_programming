#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        best_score = 0
        best_key = ""
        for key in a_dictionary:
            if a_dictionary[key] > best_score:
                best_score = a_dictionary[key]
                best_key = key
            elif key not in a_dictionary:
                return None
    return best_key
