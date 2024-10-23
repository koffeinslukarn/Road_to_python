def new_board():
    board = {}
    return board


def is_free(board, x, y):
    if (x, y) in board:
        return False
    else:
        return True

def place_piece(board, x, y, player):
    if is_free(board, x, y) == True:
        board[x, y] = player
        return True
    else:
        return False
    
def get_piece(board, x, y):
    if (x, y) in board:
        player = board[(x, y)]
        return player
    else:
        return False
    
def remove_piece(board, x, y):
    if (x, y) in board:
        del board[(x, y)] 
        return True
    else:
        return False
    
def move_piece(board, x, y, x2, y2):
    if (x, y) in board:
        place_piece(board, x2, y2, board[x, y])
        remove_piece(board, x, y)
        return True
    else:
        return False
    


def count(board, col_row, x_y, player):
    result = 0
    for position in board:
        if board[position] == player:
            if col_row == "column" and position[0] == x_y:
                result += 1
            elif col_row == "row" and position[1] == x_y:
                result += 1
    
    return result


def nearest_piece(board, x, y):
    nearest = ()
    min_distance = float('inf')  
    for position in board:
        (piece_x, piece_y) = position
        distance = ((piece_x - x)**2 + (piece_y - y)**2)

        if distance < min_distance:
            min_distance = distance
            nearest = position

    return nearest

board = new_board()

print(is_free(board, 500, 100))

print(place_piece(board, 500, 100, "spelare1"))

print(place_piece(board, 1, 100, "spelare2"))

print(place_piece(board, 500, 100, "spelare2"))

print(place_piece(board, 500, 200, "spelare2"))

print(is_free(board,500, 100))

print(get_piece(board, 500, 100))

print(get_piece(board, 666, 666))

print(remove_piece(board, 500, 100))

print(remove_piece(board, 1, 1))

print(is_free(board, 500, 100))

print(move_piece(board, 500, 200, 500, 100))

print(get_piece(board, 500, 100))

print(count(board, "column", 500, "spelare2"))

print(count(board,"row", 100, "spelare2"))

print(nearest_piece(board, 500, 105))



def choose(n, k):
    if k == 0 or k == n:
        return 1
    if k == 1 or k == n-1:
        return n
    return n * choose(n-1, k-1) // k

print(choose(5, 3))
print(choose(1000, 1))
print(choose(52, 5))
print(choose(1000, 4))
print(choose(1000, 800))
print(choose(1000, 999))


        


        

            
        
        
        
        
    
    







    




    


    
    









    