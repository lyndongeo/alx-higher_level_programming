#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
mesg = "Last digit of"
if int(last_digit) > 5:
    print("{} {} is {} and is greater than 5".format(mesg,number, last_digit))
elif int(last_digit) == 0:
    print("{} {} is {} and is 0".format(mesg, number, last_digit))
elif int(last_digit) < 6 != 0:
    print("{} {} is {} and is less than 6 and not 0".format(mesg, number, last_digit))
