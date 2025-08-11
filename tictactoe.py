"""
Tic Tac Toe Player
"""

import math
import util
import copy 

# These are used to define the symbol user selected
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, 'X', 'O'],
            ['O', 'X', EMPTY],
            ['X', EMPTY, 'O']]

    #return [[EMPTY, EMPTY, EMPTY],
            #[EMPTY, EMPTY, EMPTY],
            #[EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    playerX = 0
    playerO = 0 

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                playerX += 1
            if board[i][j] == 'O':
                playerO += 1

    
    if playerX == playerO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

     # Initialize an empty set
    availableSquares = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                availableSquares.add((i,j))
    
    print(availableSquares)
    print(board)
    return(availableSquares)
   


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #TODO figure out why it isnt working if it is on top of the file
    import copy
    #test_board = [['X', 'X', None], ['X', 'O', None], ['O', 'X', 'O']]
    # Fetch if the user is X or O
    user = player(board)
    # Obtain the coordinates as values
    i, j = action
    # Make a deep copy of the board
    copy = copy.deepcopy(board)
    # Add the new selection to the board
    if copy[i][j] == None:
        copy[i][j]=user
    else:
        print("Square not available")
        raise ValueError

    return copy
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # returns either X, O or None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # FOR TESTING: check the number of abailable sets
    # FOR ACTUAL IMPLEMENTATION - need to check if a user has achieved 3 in a row!
    # need a way to evaluate the board for 3 in a row scenario...
    if len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    import numpy as np
    
    # I guess here the adjesiant pieces are evaluated...?
    # Fetch the user
    # Calculate the sum of rows, columns and the 2 diaogonals
    # where X = 1, O = -1 and None = 0
    # Return 1, -1 or 0
    numericalBoard = initial_state()

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                numericalBoard[i][j] = 0
            if board[i][j] == 'X':
                numericalBoard[i][j] = 1
            if board[i][j] == 'O':
                numericalBoard[i][j] = -1
    
    print(numericalBoard)
    # sum rows
    list_rows = [sum(i) for i in numericalBoard]
    if list_rows.count(3) > 0:
        print("WINNERS")
    rows =sum(list_rows)
    print(list_rows)
    print(f"rows:{rows}")

    # sum columns
    a = np.array(numericalBoard) # Converting `a` to numpy array
    list_columns = np.sum(a, axis=0).tolist()
    if list_columns.count(3) > 0:
        print("WINNERS")
    columns = sum(list_columns)
    print(list_columns)
    print(f"colums:{columns}")
    # sum diaginals
    diag1 = numericalBoard[0][0] + numericalBoard[1][1] + numericalBoard[2][2]
    diag2 = numericalBoard[0][2] + numericalBoard[1][1] + numericalBoard[2][0]
    if diag1 == 3 or diag1 == -3 or diag2 == 3 or diag2 == -3:
        print("WINNERS")
    diags = diag1+diag2
    print(f"digs:{diags}")
    # sum all
    all = rows+columns+diags
    print(all)
    raise NotImplementedError

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Fetch the user 
    # fetch avaiable sets and add to frontier?
    # Select a node to explore
    # Calculate the sum of rows, columns and the 2 diaogonals
    # where X = 1, O = -1 and None = 0
    # Different statuses will have differents sums...
    # The target is defined by the selection of the player - player O aims for -1 or 0 result,
    # player X aims for 1 or 0 result.


    availableOption = actions(board)
    print(availableOption)
    move = list(availableOption)[0]
    utility(board)

    return move
    raise NotImplementedError
