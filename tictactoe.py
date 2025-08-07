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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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
    # check the number of abailable sets
    if len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # I guess here the adjesiant pieces are evaluated...?
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # I think utility is used here to help to determine when selection for action is used
    # The target is defined by the selection of the player - player O aims for -1 or 0 result,
    # player X aims for 1 or 0 result.

    availableOption = actions(board)
    print(availableOption)
    move = list(availableOption)[0]

    return move
    raise NotImplementedError
