# -*- coding: utf-8 -*-
"""

"""


import random
 
number = random.randrange(1, 20)
playing = True
    
guess = int(input('Please enter your first guess (1-20): '))

while playing:
    
    if guess < number:
        print('Your guess is too low')
        guess = int(input('Please try again: '))
        
    elif guess > number:
        print('Your guess is too high')
        guess = int(input('Please try again: '))
    
    else:
        print('Hit!')
        playing = False


    