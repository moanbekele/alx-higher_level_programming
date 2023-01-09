#!/usr/bin/python3

def replace_in_list(the_list, idx, element):
    if idx < 0 or idx >= len(the_list):
        return the_list
    the_list[idx] = element
    return the_list
