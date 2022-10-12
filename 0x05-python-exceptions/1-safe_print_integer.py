#!/usr/bin/python3

def safe_print_integer(value):
    printed = False
    try:
        print("{:d}".format(value))
        printed = True
    except Exception:
        printed = False

    return printed
