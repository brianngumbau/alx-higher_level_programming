#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdir = a_dictionary.copy()
    listkeys = list(newdir.keys())

    for x in listkeys:
        newdir[x] *= 2

    return (newdir)
