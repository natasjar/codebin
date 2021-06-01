"""
Created on Mon May 24 17:01:15 2021

@author: Natasja Hopkin
"""
from random import randint

def transpose(board):
    #transpose the board to treat columns like rows
    return [''.join(row[n] for row in board) for n in range(3)]

def place(board, counter, x, y):  
    board = [row[:x] + counter + row[x+1:] if row_number == y else row for row_number, row in enumerate(board)]
    return board

#find win conditions to play 
def win_for(board, counter):
    three = counter*3
    #straight rows and columns or diagonals
    #returns boolean true if win false if not
    return any(row == three for row in board) or \
        any(row == three for row in transpose(board)) or (
            board[1][1] == counter and (
                board[0][0] == board[2][2] == counter or board[2][0] == board[0][2] == counter))

#accounts for the roles are swapped and computer goes second not first 
def best_move(board, moves, counter):
    #code goes first
    other = 'o'
    
    draw_pos = None
    for y in range(3):
        for x in range(3):
            if board[y][x] != ' ':
                continue

            any_pos = x, y
            updated = place(board, counter, x, y)
            
            #place any potential winning move
            if win_for(updated, counter):
                return (x, y), 'win'
            
            # board full after this move
            if moves == 8:    
                return (x, y), 'draw'

            #check for other player to counter their moves
            _, result = best_move(updated, moves + 1, other)
            if result == 'lose':
                return (x, y), 'win'

            if result == 'draw' and not draw_pos:
                draw_pos = x, y
    return (draw_pos, 'draw') if draw_pos else (any_pos, 'lose')

def pretty_print_board(board):
    print('---+---+---\n'.join(' %s \n' % ' | '.join(r) for r in board))
    
def play():
    user_counter = "o"
    computer_counter = 'x' 
    print('You are "o"s')
    board = [' '*3]*3 
    #board is represented as below
    # ['   ', '   ', '   ']
    # ['   ', '   ', '   ']
    # ['   ', '   ', '   ']
    
    moves = 0
    
    
    board = place(board, 'x', randint(0, 2), randint(0, 2))
    moves += 1
    pretty_print_board(board)

    while True:
        while True:
            #type moves x,y
            player_move = input()
            nums = player_move.split(',')
            if len(nums) == 2:
                try:
                    x, y = int(nums[0]), int(nums[1])
                    if board[y][x] == ' ':
                        break
                except (IndexError, ValueError):
                    pass

            print("invalid move")

        board = place(board, user_counter, x, y)
        moves += 1
        if win_for(board, user_counter):
            pretty_print_board(board)
            print('You win')
            return

        if moves == 9:
            pretty_print_board(board)

            print('Draw')
            return
   
        (x, y), r = best_move(board, moves, computer_counter)
        board = place(board, computer_counter, x, y)
        moves += 1
        pretty_print_board(board)

        if win_for(board, computer_counter):
            print('Computer win')
            return

        if moves == 9:
            print('Draw')
            return
play()