# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s): Spencer Enriquez, John Fogerson
#
# ----------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation

Your task for homework 4 is to implement:
1.  astar
2.  single_heuristic
3.  better_heuristic
4.  gen_heuristic
"""
import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    closed = set()  # keep track of our explored
    fringe = data_structures.PriorityQueue()  # for A*, the fringe is a Priority queue
    state = problem.start_state()
    root = data_structures.Node(state, None, None)
    fringe.push(root, root.cumulative_cost)
    while not fringe.is_empty():
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.solution()  # we found a solution
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.expand(node.state):
                f = node.cumulative_cost + action_cost + heuristic(child_state, problem)
                child_node = data_structures.Node(child_state, node, action, node.cumulative_cost + action_cost)
                fringe.push(child_node, f)
    return None


def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    Heuristic used with A* to find Manhattan distance from single medal
    Running A* with this single heuristic, gives us better performance than uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: Manhattan Distance between Sammy and medal, 0 if no medals left
    """
    (pos, medals) = state
    #print(f'pos = {pos}, medals = {medals}')
    if medals:
        #print(abs(medals[0][0] - pos[0]) + abs(medals[0][1] - pos[1]))
        return abs(medals[0][0] - pos[0]) + abs(medals[0][1] - pos[1])

    else:
        return 0


def better_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    pass


def gen_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    pass