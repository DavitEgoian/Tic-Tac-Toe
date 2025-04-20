def draw_board(spots):
    board = f'''-------------\n| {spots[1]} | {spots[2]} | {spots[3]} |\n-------------\n| {spots[4]} | {spots[5]} | {spots[6]} |\n-------------\n| {spots[7]} | {spots[8]} | {spots[9]} |\n-------------'''
    print(board)

def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'