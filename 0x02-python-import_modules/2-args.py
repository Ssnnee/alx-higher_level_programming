#!/usr/bin/python3

def arg_printer(argv):
    num_args = len(argv) - 1
    if num_args == 0:
        print("{:d} argument".format(num_args))
        return
    else:
        if num_args == 1:
            print("{:d} argument:".format(num_args))
        else:
            print("{:d} arguments:".format(num_args))
        for i in range(1, num_args + 1):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    import sys
    arg_printer(sys.argv)
