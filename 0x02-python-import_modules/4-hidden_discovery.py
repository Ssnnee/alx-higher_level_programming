#!/usr/bin/python3
def search():
    found = dir(hidden_4)
    for i in found:
        if i[:2] != "__":
            print("{:s}".format(i))


if __name__ == "__main__":
    search()
