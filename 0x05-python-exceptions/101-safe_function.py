#!/usr/bin/python3
import sys
# from sys import stderr
# two solutions


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
        # exec = fct(*args)
        # return exec
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
        # print("Exception: {}".format(error), file=stderr)
        # exec = None
