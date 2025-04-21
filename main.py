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
    user_choice = input(f"Player {(turn%2) + 1}'s turn: Pick your spot or type 'quit' to quit the game: ").lower()
    if user_choice == 'quit':
        playing = False
        print('You have quited the game.')
    else:
        try:
            user_choice = int(user_choice)
        except ValueError:
            print('Please enter a valid number!')
        else:
            if int(user_choice) in spots:
                if not spots[int(user_choice)] in {'X', 'O'}:
                    turn += 1
                    spots.update({int(user_choice): check_turn(turn)})
                else:
                    print('You have already chose this spot please try again with a different one')

