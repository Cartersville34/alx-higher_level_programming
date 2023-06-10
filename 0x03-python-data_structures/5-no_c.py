#!/usr/bin/python3

def no_c(My_string):
    updated_str = ''
    for i in My_string:
        if i != 'c' and i != 'C':
            updated_str += i
    return (updated_str)
