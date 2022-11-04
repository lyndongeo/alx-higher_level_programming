#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 and i % 5):
            print("%s%s" % (FIZZ, BUZZ), end=' ')
        elif (i % 3):
            print("%s" % (FIZZ), end=' ')
        elif (i % 5):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (i), end=' ')
