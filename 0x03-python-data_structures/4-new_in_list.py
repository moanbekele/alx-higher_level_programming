#!/usr/bin/python3


def new_in_list(the_list, idx, element):
    if idx < 0 or idx >= len(the_list):
        return the_list.copy()
    new_list = the_list.copy()
    new_list[idx] = element
    return new_list
