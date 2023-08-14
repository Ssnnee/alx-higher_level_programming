#!/usr/bin/python3
for i in range(97, 123):
    letter = chr(i)
    if letter != "q" and letter != "e":
        print("{}".format(letter), end="")
