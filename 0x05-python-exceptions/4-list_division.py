#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nw_lst = []
    for j in range(0, list_length):
        try:
            division = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            nw_lst.append(division)
    return (nw_lst)
