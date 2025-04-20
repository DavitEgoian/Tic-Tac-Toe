import os
from random import choice

from board import draw_board, check_turn

spots = {1: '1', 2: '2', 3: '3', 4:'4', 5:'5',
         6: '6', 7: '7', 8: '8', 9:'9'}

playing = True
turn = 0

while playing:
    os.system("cls")
    draw_board(spots)
    user_choice = input('').lower()
    if user_choice == 'quit':
        playing = False
        print('You have quited the game.')
    else:
        try:
            user_choice = int(user_choice)
        except ValueError:
            print('Please enter a valid number!')
        else:
            turn += 1
            spots.update({int(user_choice): check_turn(turn)})

