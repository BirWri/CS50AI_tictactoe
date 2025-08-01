"""
Tic Tac Toe Player
"""

import math
import util

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
                playerX =+1
            if board[i][j] == 'O':
                playerO =+1

    print(playerX)
    print(playerO)
    
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
    return(availableSquares)
   


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    #test_board = [['X', 'X', None], ['X', 'O', None], ['O', 'X', 'O']]
    user = player(board)

    i, j = action
    print(f"in result function user:{user}")
    import copy 
    copy = copy.deepcopy(board)
    copy[i][j]=user

    print(board)
    print(copy)

    return copy
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # For testing I set it False, so the game would continue
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    availableOption = actions(board)
    print(availableOption)
    move = list(availableOption)[0]

    return move
    raise NotImplementedError
