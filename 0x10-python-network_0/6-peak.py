#!/usr/bin/python3
"""
findpeak module
"""

def peak_alg(arr, low, high, n):
    """ algorithm"""

    mid = (low + high) /2
    mid = int(mid)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
       (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]

    elif (mid > 0 and arr[mid + 1] > arr[mid]):
        return peak_alg(arr, (mid + 1), high, n)

    else:
        return peak_alg(arr, low, (mid - 1), n)



def find_peak(list_of_integers):
    """ finds a peak in an array """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    n = len(list_of_integers)
    res = peak_alg(list_of_integers, 0, n - 1 , n)
    return res


"""
def find_peak(list_of_integers):
    function to find the peak element in a list
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for item in list_of_integers:
            if item > peak:
                peak = item
        return peak
"""
