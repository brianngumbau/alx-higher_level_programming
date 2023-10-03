#!/usr/bin/python3
for integer in range(0, 100):
    if integer == 99:
        print("{}".format(integer))
    else:
        print("{:02}".format(integer), end=", ")
