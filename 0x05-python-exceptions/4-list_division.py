#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    total = 0
    for i in range(0, list_length):
        try:
            total = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except ValueError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            res_list.append(total)
    return (res_list)
