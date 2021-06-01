#priorities

# board = [[""]*6]*6

#     = [['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', ''], ['', '', '', '', '', '']]
    
#     with random apples 

#player stored in position (x,y)
def move(board, player):
    fruit_locations = []
    
    #iterate over every space in the board 
    for i, row in enumerate(board):
        for j, space in enumerate(row):
            if board[i][j] == "*":
                #track location of fruit
                fruit_locations.append((i,j))
    
    print(fruit_locations)
    
    
    closest_fruit_distance = None
    #for every fruit
    for fruit in fruit_locations:
        if fruit == player: #take fruit if player is in same spot as fruit
            return "TAKE" #return takes out of function so ends move
        
        #otherwise, find closest fruit to move towards
        #distance from player_pos 
        distance = (player[0] - fruit[0], player[1] - fruit[1])
        if not closest_fruit_distance:
            closest_fruit_distance = distance
            closest_fruit = fruit
        elif distance < closest_fruit_distance:
            closest_fruit_distance = distance
            closest_fruit = fruit
     
    #Once iterated over, have closest fruit, move towards
    if closest_fruit[0] > player[0]:
        return "NORTH"
    elif closest_fruit[1] > player[1]:
        return "EAST"
    elif closest_fruit[0] < player [0]:
        return "SOUTH"
    elif closest_fruit[1] < player[1]:
        return "WEST"
        
board = [['', '*', '', '', '', ''], 
         ['', '', '', '', '', ''], 
         ['', '', '', '', '', ''], 
         ['', '', '', '', '', ''], 
         ['', '', '', '', '', ''], 
         ['', '', '', '', '', '']]     
print(move(board,(0,0)))
    