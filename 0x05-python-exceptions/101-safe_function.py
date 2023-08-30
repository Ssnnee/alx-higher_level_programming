#!/usr/bin/python3
def safe_function(fct, *args):
    """This function executes a function safely."""
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    return res
