#!/usr/bin/python3

def multiple_returns(phrase):
    if phrase != '':
        first_char = phrase[0]
    else:
        first_char = None
    return (len(phrase), first_char)
