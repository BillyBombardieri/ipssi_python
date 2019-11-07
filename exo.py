#!/usr/bin/python3

import datetime
date = datetime.datetime.now()


def mean(a,b):
    return((a+b)/2)

print(mean(5,6))


def pairimpair(a):
    if (a%2)==0:
        print("Nous sommes le",a,"et c'est jour pair")
    else:
        print("Nous sommes le",a,"et c'est un jour impair")

pairimpair(date.day)


