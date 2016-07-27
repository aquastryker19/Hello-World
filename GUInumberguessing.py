# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:37:32 2016

@author: pi
"""

import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0

easygui.msgbox('''i got a seeecret and ya got 6 tries...''')
while guess != secret and tries < 6:
    guess = easygui.integerbox('wats yer guess mate???')
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + 'toooo lowww lolololol')
    elif guess > secret:
        easygui.msgbox(str(guess) + 'toooo highhhhh lolololol')
    tries = tries +1

if guess == secret:
    easygui.msgbox('dang it!! ye got it...')
else:
    easygui.msgbox('yer outta guesses!lolololololol it was', secret)
