#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for item in my_list[:x]:
        try:
            if item is not my_list[-1] and x - 1 > i:
                print("{}".format(item), end="")
            else:
                print("{}".format(item), end='\n')
            i += 1
        except:
            break;
    return (i)
