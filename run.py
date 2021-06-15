from tkinter import Widget
import pygame
import math
#import board
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from pygame.scrap import lost, put
from game import *

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode([1500, 1000])

class State(object):
    def __init__(self):
        self.addingTigers = True
        self.addingGoats = False
        self.tigersMove = False
        self.addedGoats = 0
        self.leftGoats = 18
        self.lostGoats = 0
        self.board = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]


def init():
    state = State()

    initial_board_state = GameState(state=state, next_to_move=1)
    root = MonteCarloTreeSearchNode(state=initial_board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(100)
    c_state = best_node.state
    c_board = c_state.board
    return c_state, c_board

def get_action(state):
    try:
        location = input("Your move: ")
        if isinstance(location, str):
            location = [int(n, 10) for n in location.split(",")]
        if len(location) != 2:
            return -1
        x = location[0]
        y = location[1]
        move = GameMove(x, y, -1)
    except Exception as e:
        move = -1
    if move == -1 or not state.is_move_legal(move):
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


c_state,c_board = init()
print(c_board)


while True:
    move1 = get_action(c_state)
    c_state = c_state.move(move1)
    c_board = c_state.board
    print(c_board)

    board_state = GameState(state=c_board, next_to_move=1)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(1000)
    c_state = best_node.state
    c_board = c_state.board
    print(c_board)
    if judge(c_state)==1:
        break
    elif judge(c_state)==-1:
        continue