from copy import Error
from tkinter import Widget
from numpy import who
import pygame
import math
#import board
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from pygame.scrap import lost, put
from game import *
from state import *

def init():
    state = State()

    initial_board_state = GameState(state=state, next_to_move=1)

    print("Poczatkowy")
    state.print()

    root = MonteCarloTreeSearchNode(state=initial_board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)

    best_node = mcts.best_action(10)
    c_state = best_node.state
    state_copy = c_state.state

    board_state = GameState(state=state_copy, next_to_move=1)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(10)
    c_state = best_node.state

    return c_state
    # , c_board

def get_action(state):
    try:
        if state.state.addedGoats < 18:
            location = input("Where do you want to place a goat?")
            if isinstance(location, str):
                location = [int(n, 5) for n in location.split(",")]
            if len(location) != 2:
                return -1
            x = location[1]
            y = location[0]
            move = GameMove(2, y, x, y, x)
        else:
            location = input("Your move: ")
            if isinstance(location, str):
                location = [int(n, 5) for n in location.split(",")]
            if len(location) != 2:
                return -1
            x = location[1]
            y = location[0]
            move = GameMove(2, y, x, y, x)
    except Exception as e:
        move = -1
    # if move == -1 or not state.is_move_legal(move):
    if move == -1:
        print("invalid move")
        move = get_action(state)
    return move


def judge(state):
    if state.is_game_over():
        if state.game_result == 1.0:
            print("You lose!")
        if state.game_result == 0.0:
            print("Tie!")
        if state.game_result == -1.0:
            print("You Win!")
        return 1
    else:
        return -1



c_state = init()
# , c_board
print("Po ruchach")
c_state.state.print()

while True:
    check = True
    while check == True:
        check = False
        try:
            move1 = get_action(c_state)
            c_state = c_state.move(move1)
        except:
            check = True

    state_copy = c_state.state
    c_state.state.print()

    board_state = GameState(state=state_copy, next_to_move=1)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(10)
    c_state = best_node.state

    # c_board = c_state.state.board
    c_state.state.print()
    if judge(c_state)==1:
        break
    elif judge(c_state)==-1:
        continue