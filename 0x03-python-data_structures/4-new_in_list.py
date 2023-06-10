#!/usr/bin/python3

def new_in_list(my_list, index, element):
    if my_list:
        if index < 0 or index >= len(my_list):
            return my_list
        else:
            new_list = my_list.copy()
            new_list[index] = element
            return new_list
