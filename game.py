import copy
import random
import sys

import numpy as np

#from board import Board

move_goats_connections = {
    0: [1, 5, 6], 1: [2, 0, 6], 2: [3, 1, 7, 6, 8], 3: [4, 2, 8], 4: [3, 9, 8],
    5: [6, 10, 0], 6: [7, 5, 11, 1, 10, 2, 12, 0], 7: [8, 6, 12, 2], 8: [9, 7, 13, 3, 12, 4, 14, 2], 9: [8, 14, 4],
    10: [11, 15, 5, 6, 16], 11: [12, 10, 16, 6], 12: [13, 11, 17, 7, 16, 8, 18, 6], 13: [14, 12, 18, 8],
    14: [13, 19, 9, 18, 8],
    15: [16, 20, 10], 16: [17, 15, 21, 11, 20, 12, 22, 10], 17: [18, 16, 22, 12],
    18: [19, 17, 23, 13, 22, 14, 24, 12], 19: [18, 24, 14],
    20: [21, 15, 16], 21: [22, 20, 16], 22: [23, 21, 17, 18, 16], 23: [24, 22, 18], 24: [23, 19, 18]
}

move_tigers_connections = {
    0: [5, 10, 15, 20, 1, 2, 3, 4, 6, 12, 18, 24],
    1: [0, 6, 11, 16, 21, 2, 3, 4],
    2: [0, 1, 3, 4, 6, 10, 8, 14, 7, 12, 17, 23],
    3: [0, 1, 2, 4, 8, 13, 18, 23],
    4: [0, 1, 2, 3, 8, 12, 16, 20, 9, 14, 19, 24],
    5: [0, 10, 15, 20, 6, 7, 8, 9],
    6: [5, 0, 10, 1, 2, 7, 8, 9, 11, 16, 21, 12, 18, 24],
    7: [2, 5, 6, 12, 17, 22, 8, 9],
    8: [2, 3, 4, 9, 14, 13, 18, 23, 12, 16, 20, 5, 6, 7],
    9: [4, 5, 6, 7, 8, 9, 14, 19, 24],
    10: [0, 5, 6, 2, 11, 12, 13, 14, 16, 22, 15, 20],
    11: [10, 1, 6, 12, 13, 14, 16, 21],
    12: [0, 6, 2, 7, 4, 8, 13, 14, 18, 24, 17, 22, 16, 20, 10, 11],
    13: [3, 8, 14, 18, 23, 10, 11, 12],
    14: [4, 9, 2, 8, 10, 11, 12, 13, 18, 22, 19, 24],
    15: [0, 5, 10, 16, 17, 18, 19, 20],
    16: [10, 1, 6, 11, 4, 8, 12, 17, 18, 19, 22, 21, 20, 15],
    17: [15, 16, 2, 7, 12, 18, 19, 22],
    18: [0, 6, 12, 3, 8, 13, 14, 19, 24, 23, 22, 15, 16, 17],
    19: [4, 9, 14, 24, 15, 16, 17, 18],
    20: [0, 5, 10, 15, 4, 8, 12, 16, 21, 22, 23, 24],
    21: [20, 1, 6, 11, 16, 22, 23, 24],
    22: [20, 21, 10, 16, 2, 7, 12, 17, 14, 18, 23, 24],
    23: [20, 21, 22, 3, 8, 13, 18, 24],
    24: [20, 21, 22, 23, 0, 6, 12, 18, 4, 9, 14, 19],
}

capture_connections = {
    0: [2, 10, 12], 1: [3, 11], 2: [4, 0, 12, 10, 14], 3: [1, 13], 4: [2, 14, 12],
    5: [7, 15], 6: [8, 16, 18], 7: [9, 5, 17], 8: [6, 18, 16], 9: [7, 19],
    10: [12, 20, 0, 2, 22], 11: [13, 21, 1], 12: [14, 10, 22, 2, 20, 4, 24, 0],
    13: [11, 23, 3], 14: [12, 24, 4, 22, 2],
    15: [17, 5], 16: [18, 6, 8], 17: [19, 15, 7], 18: [16, 8, 6], 19: [17, 9],
    20: [22, 10, 12], 21: [23, 11], 22: [24, 20, 12, 14, 10], 23: [21, 13], 24: [22, 14, 12]
}

block_checker = {
    0: [5, 10, 6, 12, 1, 2],
    1: [0, 6, 11, 2, 3],
    2: [0, 1, 6, 10, 7, 12, 8, 14, 3, 4],
    3: [1, 2, 8, 13, 4],
    4: [2, 3, 8, 12, 9, 14],
    5: [0, 6, 7, 10, 15],
    6: [0, 5, 10, 1, 11, 16, 2, 7, 8, 12, 18],
    7: [5, 6, 2, 12, 17, 8, 9],
    8: [2, 6, 7, 12, 16, 3, 13, 18, 4, 9, 14],
    9: [7, 8, 4, 14, 19],
    10: [0, 5, 15, 20, 2, 6, 16, 22, 11, 12],
    11: [10, 1, 6, 16, 21, 12, 13],
    12: [0, 6, 10, 11, 20, 16, 2, 7, 17, 22, 4, 8, 13, 14, 18, 24],
    13: [11, 12, 3, 8, 18, 23, 14],
    14: [2, 8, 12, 13, 18, 22, 4, 9, 19, 24],
    15: [5, 10, 20, 16, 17],
    16: [10, 15, 20, 6, 11, 21, 12, 8, 17, 18, 22],
    17: [15, 16, 7, 12, 22, 18, 19],
    18: [6, 12, 16, 17, 22, 8, 13, 23, 14, 19, 24],
    19: [17, 18, 9, 14, 24],
    20: [10, 15, 16, 12, 21, 22],
    21: [20, 11, 16, 22, 23],
    22: [20, 21, 10, 16, 12, 17, 14, 18, 23, 24],
    23: [21, 22, 13, 18, 24],
    24: [22, 23, 12, 18, 14, 19],
}

class GameMove(object):
    def __init__(self, value, posY, posX, destY, destX):
        self.pos_from = [posY, posX]
        self.pos_to = [destY, destX]
        self.value = value

    def __repr__(self):
        return "from:" + str(self.pos_from) + " to:" + str(self.pos_to) + " v:" + str(self.value)


class GameState(object):
    P1 = 1
    P2 = -1
    
    def __init__(self, state, next_to_move=1, c_move=None):
        self.state = state #tu jest wszystko kuny jenoty dziki jelenie ogarnąć to i podmienić z board
        self.board = state.board
        self.board_size = 5
        self.next_to_move = next_to_move
        self.current_move = c_move

    @property
    def game_result(self):
        # check if game is over
        status = self.board.checkStatus()
        if status == 1:
            return 1.
        elif status == -1:
            return -1.
        else:
            # if not over - no result
            return None

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        if(self.next_to_move == GameState.P1):
            return self.check_move_tiger(self.board, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])     
        else:
            return self.check_move_goat(self.board, move.pos_from[0], move.pos_from[1], move.pos_to[0], move.pos_to[1])
                
    def move(self, move):
        if not self.is_move_legal(move):
            raise ValueError("move " + move + " on board " + self.board + " is not legal")
        new_board = copy.deepcopy(self.board)
        new_board[move.pos_to[0], move.pos_to[1]] = move.value
        new_board[move.pos_from[0], move.pos_from[1]] = 0
        next_to_move = GameState.P2 if self.next_to_move == GameState.P1 else GameState.P1
        return GameState(new_board, next_to_move, move)

    def check_move_tiger(self, board, posY, posX, destY, destX):
        possible_move = False
        for capture_move in capture_connections[posX * 5 + posY]:
            if capture_move == destX * 5 + destY and board[destY][destX] == 0 and board[int((destY + posY) / 2)][int((destX + posX) / 2)] == 2:
                possible_move = True

        for normal_move in move_tigers_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and board[destY][destX] == 0 and self.checkRoad(board, posX, posY, destX, destY) == True:
                possible_move = True

        return possible_move

    def checkRoad(self, board, tigerX, tigerY, destX, destY):
        tempX = destX
        tempY = destY
        while tempX != tigerX or tempY != tigerY:
            if board[tempY][tempX] == 1:
                return False
            if destY == tigerY and destX > tigerX:
                tempX = tempX - 1
            elif destY == tigerY and destX < tigerX:
                tempX = tempX + 1
            elif destX == tigerX and destY < tigerY:
                tempY = tempY + 1
            elif destX == tigerX and destY > tigerY:
                tempY = tempY - 1
            elif destX > tigerX and destY > tigerY:
                tempX = tempX - 1
                tempY = tempY - 1
            elif destX < tigerX and destY > tigerY:
                tempX = tempX + 1
                tempY = tempY - 1
            elif destX > tigerX and destY < tigerY:
                tempX = tempX - 1
                tempY = tempY + 1
            elif destX < tigerX and destY < tigerY:
                tempX = tempX + 1
                tempY = tempY + 1
            if board[tempY][tempX] == 2:
                return False
        return True

    def check_move_goat(self, board, posY, posX, destY, destX):
        possible_move = False
        for normal_move in move_goats_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and board[destY][destX] == 0:
                possible_move = True
        return possible_move

    def checkIfTigersBlocked(self, board):
        for x in range(5):
            for y in range(5):
                if board[y][x] == 1:
                    for neighbour in block_checker[x * 5 + y]:
                        if board[int(neighbour / 5)][int(neighbour % 5)] == 0:
                            return False
        return True   

    def get_possible_moves_tiger(self, board, posX, posY):
        possible = []
        for x in range(5):
            for y in range(5):
                if self.check_move_tiger(board, posX, posY, x, y) == True:
                    possible.append([x, y])
        return possible

    def get_possible_moves_goat(self, board, posX, posY):
        possible = []
        for x in range(5):
            for y in range(5):
                if self.check_move_goat(board, posX, posY, x, y) == True:
                    possible.append([x, y])
        return possible

    def getPossibleGoatPlaces(self, board):
        possibleGoatPlaces = []
        for x in range(5):
            for y in range(5):
                if board[y][x] == 0:
                    possibleGoatPlaces.append([y, x])
        return possibleGoatPlaces

    def getPossibleTigerPlaces(self, board):
        possibleTigerPlaces = []
        for x in range(5):
            for y in range(5):
                if board[y][x] == 0 and x > 0 and y > 0 and x < 4 and y < 4:
                    possibleTigerPlaces.append([y, x])
        return possibleTigerPlaces