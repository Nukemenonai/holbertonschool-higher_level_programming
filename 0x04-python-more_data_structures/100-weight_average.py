#!/usr/bin/python3
def weight_average(my_list=[]):
    avg = 0
    dvdr = 0
    if not my_list:
        return 0
    else:
        for i in my_list:
            avg += (i[0]*i[1])
            dvdr += (i[1])
        return avg / dvdr
