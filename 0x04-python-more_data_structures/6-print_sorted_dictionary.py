#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listord = list(a_dictionary.keys())
    listord.sort()
    for y in listord:
        print("{}: {}".format(y, a_dictionary.get(y)))
