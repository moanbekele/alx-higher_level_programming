#!/usr/bin/python3

def print_reversed_list_integer(the_list=[]):
    if the_list:
        for i in reversed(the_list):
            print("{:d}".format(i))
