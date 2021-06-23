import copy
import random
import sys

import numpy as np

#from board import Board
class GameMove(object):
    def __init__(self, value, posY, posX, destY, destX):
        self.pos_from = [posY, posX]
        self.pos_to = [destY, destX]
        self.value = value

    def __repr__(self):
        return "pos_from:" + str(self.pos_from) + "\npos_to:" + str(self.pos_to) + "\nvalue:" + str(self.value) + "\n"


class GameState(object):
    P1 = 1
    P2 = -1
    
    def __init__(self, state, next_to_move=1, c_move=None):
        self.state = state
        self.board_size = 5
        self.next_to_move = next_to_move
        self.current_move = c_move

    @property
    def game_result(self):
        status = self.state.check_status()
        if status == 2:
            return 2.
        elif status == 1:
            return 1.
        else:
            # if not over - no result
            return None

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        if(self.next_to_move == GameState.P1):
            return self.state.check_move_tiger(self.state.board, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])     
        else:
            return self.state.check_move_goat(self.state.board, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])
                
    def move(self, move):
        new_state = copy.deepcopy(self.state)
        #rozstawianie
        if self.state.addingTigers > 0:
            new_state, succed = self.state.add_tiger(new_state, move.pos_to[0], move.pos_to[1])
            if not succed:
                # raise ValueError("move " + move + " on board " + self.state.board + " is not legal")
                raise ValueError("move is not legal")
            if new_state.addingTigers > 0:
                next_to_move = GameState.P1
            else:
                next_to_move = GameState.P2
            return GameState(new_state, next_to_move, move)

        elif self.state.addingGoats == True and self.next_to_move == GameState.P2:
            new_state, succed = self.state.add_goat(new_state, move.pos_to[0], move.pos_to[1])
            if not succed:
                # raise ValueError("move " + move + " on board " + self.state.board + " is not legal")
                raise ValueError("move is not legal")
            next_to_move = GameState.P1
            return GameState(new_state, next_to_move, move)

        else:
            if not self.is_move_legal(move):
                # raise ValueError("move " + move + " on board " + self.state.board + " is not legal")
                raise ValueError("move  is not legal")
            #dla którego gracza
            if(self.next_to_move == GameState.P1):
                # self.state.print()
                new_state = self.state.move_tiger(new_state, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])
            else:
                new_state = self.state.move_goat(new_state, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])

            next_to_move = GameState.P2 if self.next_to_move == GameState.P1 else GameState.P1
            return GameState(new_state, next_to_move, move)

    def get_legal_actions(self):
        if self.next_to_move == GameState.P1:
            #tygrysy, sprawdź, czy rozstawiają
            if self.state.addingTigers > 0:
                return self.state.getPossibleTigerPlaces(self.state.board)
            else:
                return self.state.get_all_possible_moves_tiger(self.state)
        else:
            if self.state.leftGoats > 0:
                return self.state.getPossibleGoatPlaces(self.state.board)
            else:
                return self.state.get_all_possible_moves_goat(self.state)
