#!/usr/bin/python3
for integer in range(97, 123):
    if chr(integer) != 'q' and chr(integer) != 'e':
        print("{}".format(chr(integer)), end="")
