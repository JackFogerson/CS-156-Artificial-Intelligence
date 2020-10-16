# ----------------------------------------------------------------------
# Name:     adversarial_search
# Purpose:  Homework 6 - Implement adversarial search algorithms
#
# Author: Spencer Enriquez, John Fogerson
#
# ----------------------------------------------------------------------
"""
Adversarial search algorithms implementation
Your task for homework 6 is to implement:
1.  minimax
2.  alphabeta
3.  abdl (alpha beta depth limited)
"""
import random
import math  # You can use math.inf to initialize to infinity

def rand(game_state):
    """
    Generate a random move.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the random move
    """
    done = False
    while not done:
        row = random.randint(0, game_state.size - 1)
        col = random.randint(0, game_state.size - 1)
        if game_state.available(row,col):
            done = True
    return row, col


def minimax(game_state):
    """
    Find the best move for our AI agent using the minimax algorithm.
    (searching the entire tree from the current game state)
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """

    return max(game_state.possible_moves(), key = lambda m: value(game_state.successor(m, "AI"), "user"))

def value(game_state, agent):
    """
    Calculate the minimax value for any state under the given agent's
    control.
    :param game_state: GameState object - state may be terminal or
    non-terminal
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    if game_state.is_win("AI"):
        return 1
    elif game_state.is_win("user"):
        return -1
    elif game_state.is_tie():
        return 0
    else:
        if agent == "AI":
            return max_value(game_state)
        else:
            return min_value(game_state)


def max_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    values = []
    moves = game_state.possible_moves()
    for r, c in moves:
        values.append(value(game_state.successor((r, c), "AI"), "user"))
    return max(values)

def min_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    values = []
    moves = game_state.possible_moves()
    for r, c in moves:
        values.append(value(game_state.successor((r, c), "user"), "AI"))
    return min(values)



def alphabeta(game_state):
    """
    Find the best move for our AI agent using the minimax algorithm
    with alpha beta pruning.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    return max(game_state.possible_moves(), key = lambda m: ab_value(game_state.successor(m, "AI"), "user", -math.inf, math.inf))


def ab_value(game_state, agent, alpha, beta):
    """
    Calculate the minimax value for any state under the given agent's
    control using alpha beta pruning
    :param game_state: GameState object - state may be terminal or
    non-terminal.
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    if game_state.is_win("AI"):
        return 1
    elif game_state.is_win("user"):
        return -1
    elif game_state.is_tie():
        return 0
    else:
        if agent == "AI":
            return abmax_value(game_state, alpha, beta)
        else:
            return abmin_value(game_state, alpha, beta)


def abmax_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    v = -math.inf
    moves = game_state.possible_moves()
    for m in moves:
        v = max(v, ab_value(game_state.successor(m, "AI"), "user", alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def abmin_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    v = math.inf
    moves = game_state.possible_moves()
    for m in moves:
        v = min(v, ab_value(game_state.successor(m, "user"), "AI", alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def abdl(game_state, depth):
    """
    Find the best move for our AI agent by limiting the alpha beta
    search the given depth and using the evaluation function
    game_state.eval()
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    return max(game_state.possible_moves(), key = lambda m: abdl_value(game_state.successor(m, "AI"), "user", -math.inf, math.inf, depth))


def abdl_value(game_state, agent, alpha, beta, depth):
    """
    Calculate the utility for any state under the given agent's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: GameState object - state may be terminal or
    non-terminal
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) utility of that state
    """
    size = game_state.size*2-1
    if game_state.is_win("AI"):
        return size
    elif game_state.is_win("user"):
        return -size
    elif game_state.is_tie():
        return 0
    elif depth == 0:
        return game_state.eval()
    else:
        if agent == "AI":
            return abdlmax_value(game_state, alpha, beta, depth)
        else:
            return abdlmin_value(game_state, alpha, beta, depth)


def abdlmax_value(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Max's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    v = -math.inf
    moves = game_state.possible_moves()
    for m in moves:
        v = max(v, abdl_value(game_state.successor(m, "AI"), "user", alpha, beta, depth-1))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def abdlmin_value( game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Min's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    v = math.inf
    moves = game_state.possible_moves()
    for m in moves:
        v = min(v, abdl_value(game_state.successor(m, "user"), "AI", alpha, beta, depth-1))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
