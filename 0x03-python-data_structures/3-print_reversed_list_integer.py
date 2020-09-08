#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for data in my_list[::-1]:
            # [star:end:-1]
            # for data in reversed(my_list):
            # reversed: return a reverse iterator
            # with this method it also works
            print("{:d}".format(data))
