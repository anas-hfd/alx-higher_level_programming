#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        x = 0
        j = 0
        for ele in my_list:
            x += (ele[0] * ele[1])
            j += ele[1]
        return (x / j)
    return 0
