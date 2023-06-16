#!/usr/bin/python3
def complex_delete(my_dict, value):
    kd = []
    for keys in my_dict:
        if my_dict[keys] == value:
            kd.append(keys)
    for keys in kd:
        del my_dict[keys]
    return my_dict
