#!/usr/bin/python3
def add_arg(argv):
    num_args = len(argv) - 1
    if num_args == 0:
        print("{:d}".format(num_args))
        return
    else:
        initial = 0
        for i in range(1, num_args + 1):
            initial += int(argv[i])
        print("{:d}".format(initial))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
