#!/usr/bin/python3

def safe_print_division(a, b):
    """This function divides 2 integers and prints the result."""
    res = None
    try:
        res = a / b
    # except ZeroDivisionError:
    #     return None
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(res))
        return res
