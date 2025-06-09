"""
Tic Tac Toe Player
"""

import math
import copy

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O


def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Ação inválida")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Verifica diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)

    def max_value(state):
        if terminal(state):
            return utility(state), None
        v = float('-inf')
        best_action = None
        for action in actions(state):
            min_result, _ = min_value(result(state, action))
            if min_result > v:
                v = min_result
                best_action = action
                if v == 1:
                    break
        return v, best_action

    def min_value(state):
        if terminal(state):
            return utility(state), None
        v = float('inf')
        best_action = None
        for action in actions(state):
            max_result, _ = max_value(result(state, action))
            if max_result < v:
                v = max_result
                best_action = action
                if v == -1:
                    break
        return v, best_action

    if current_player == X:
        _, move = max_value(board)
    else:
        _, move = min_value(board)

    return move


