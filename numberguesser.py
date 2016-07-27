# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 01:12:28 2016

@author: pi
"""
'''chapter 1-skye'''

import random

secret = random.randint(1, 99)
guess = 0
tries = 0

print "AHOY! find my seeecret numberrrr..."
print "you only get 10 tries so beeewareee..."

while guess != secret and tries < 10:
    guess = input("Hwats yerrr guesss???")
    if guess < secret:
        print "toooo lowww..."
    elif guess > secret:
        print "toooooo highhhhh..."
    tries = tries + 1
if guess == secret:
    print "dang it! i don't keep secrets very well..."
else:
    print "yer outta guesses :)"
    print "ma secret wuz...", secret