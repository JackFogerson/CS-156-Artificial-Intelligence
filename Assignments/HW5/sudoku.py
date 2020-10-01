# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework5
#
# Author(s): Spencer Enriquez, Jon Fogerson
#
# ----------------------------------------------------------------------
"""
Sudoku puzzle solver implementation

q1:  Basic Backtracking Search
q2:  Backtracking Search with AC-3
q3:  Backtracking Search with MRV Ordering and AC-3
"""
import csp

# Helper function to createNeighbors, finds neighbor for specific cell
def getNeighbors(row, col):
    s = set()

    # By Row and Column
    for i in range(9):
        if i != col:
            s.add((row, i))
        if i != row:
            s.add((i, col))

    # By group
    gRow = int(row/3)
    gCol = int(col/3)
    for j in range(gRow * 3, gRow * 3 + 3):
        for k in range(gCol * 3, gCol * 3 + 3):
            if (row, col) != (j, k) and (j, k) not in s:
                s.add((j, k))
    # print(f'({row}, {col}) = {s}')
    return s

# Create Domain of values 1-9 for each cell
def createDomains(puzzle):
    domains = {}
    i = 0
    j = 0
    for i in range(9):
        for j in range(9):
            if (i, j) in puzzle.keys():
                domains[(i, j)] = {puzzle[(i, j)]}
            else:
                domains[(i, j)] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            # print(f'({i}, {j}) = {domains[(i,j)]}')
    return domains

# Calculates set of neighbors according to row, column, and grouping
def createNeighbors(puzzle):
    neighbors = {}
    i = 0
    j = 0
    for i in range(9):
        for j in range(9):
            neighbors[(i, j)] = getNeighbors(i, j)
    return neighbors

def createConstraints(var1, val1, var2, val2):
    return val1 != val2

def build_csp(puzzle):
    """
    Create a CSP object representing the puzzle.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: CSP object
    """
    return csp.CSP(createDomains(puzzle), createNeighbors(puzzle), createConstraints)


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    csp = build_csp(puzzle)
    return csp.backtracking_search(), csp

def q2(puzzle):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    csp = build_csp(puzzle)
    csp.ac3_algorithm()
    return csp.backtracking_search(), csp

def q3(puzzle):
    """
    Solve the given puzzle with backtracking search and MRV ordering and
    AC-3 as a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    csp = build_csp(puzzle)
    csp.ac3_algorithm()
    return csp.backtracking_search("MRV"), csp
