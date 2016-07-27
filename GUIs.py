# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:20:01 2016

@author: pi
"""

import easygui
flavor = easygui.buttonbox('Wats ur fav ice cream flavor?',
                  choices = ['chocolate', 'vanilla', 'mint chocoate chip', 'cookie dough'])
                  
easygui.msgbox ('ya chose' + flavor)