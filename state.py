from game import *

class State(object):
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

    def __init__(self):
        self.addingTigers = 2
        self.addingGoats = False
        self.currentPlayer = -1
        self.addedGoats = 0
        self.leftGoats = 18
        self.lostGoats = 0
        self.tigersPosition = []
        self.goatsPosition = []
        self.board = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

    def check_move_tiger(self, board, posX, posY, destX, destY):
        possible_move = False
        for capture_move in self.capture_connections[posX * 5 + posY]:
            if capture_move == destX * 5 + destY and board[destY][destX] == 0 and board[int((destY + posY) / 2)][int((destX + posX) / 2)] == 2:
                possible_move = True

        for normal_move in self.move_tigers_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and board[destY][destX] == 0 and self.checkRoad(board, posY, posX, destY, destX) == True:
                possible_move = True

        return possible_move

    def checkRoad(self, board, tigerX, tigerY, destX, destY):
        tempX = destX
        tempY = destY
        while not (tempX == tigerX and tempY == tigerY):
            try:
                if board[tempY][tempX] == 1:
                    return False
                if board[tempY][tempX] == 2:
                    return False
                if tempY == tigerY and tempX > tigerX:
                    tempX = tempX - 1
                elif tempY == tigerY and tempX < tigerX:
                    tempX = tempX + 1
                elif tempX == tigerX and tempY < tigerY:
                    tempY = tempY + 1
                elif tempX == tigerX and tempY > tigerY:
                    tempY = tempY - 1
                elif tempX > tigerX and tempY > tigerY:
                    tempX = tempX - 1
                    tempY = tempY - 1
                elif tempX < tigerX and tempY > tigerY:
                    tempX = tempX + 1
                    tempY = tempY - 1
                elif tempX > tigerX and tempY < tigerY:
                    tempX = tempX - 1
                    tempY = tempY + 1
                elif tempX < tigerX and tempY < tigerY:
                    tempX = tempX + 1
                    tempY = tempY + 1
            except Exception as e:
                print(e)
        return True

    def check_move_goat(self, board, posY, posX, destY, destX):
        possible_move = False
        for normal_move in self.move_goats_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and board[destY][destX] == 0:
                possible_move = True
        return possible_move

    def get_possible_moves_tiger(self, board, posY, posX):
        possible = []
        for x in range(5):
            for y in range(5):
                if self.check_move_tiger(board, posY, posX, y, x) == True:
                    possible.append([y, x])
        return possible

    def get_all_possible_moves_tiger(self, state):
        possible = []
        for x in range(5):
            for y in range(5):
                pion = state.board[y][x]
                if pion == 1:
                    for move in self.get_possible_moves_tiger(state.board, y, x):
                        if state.board[move[0]][move[1]] == 0:
                            possible.append(GameMove(1, y, x, move[0], move[1]))
        return possible

    def get_possible_moves_goat(self, board, posY, posX):
        possible = []
        for x in range(5):
            for y in range(5):
                if self.check_move_goat(board, posY, posX, y, x) == True:
                    possible.append([y, x])
        return possible

    def get_all_possible_moves_goat(self, state):
        possible = []
        for x in range(5):
            for y in range(5):
                pion = state.board[y][x]
                if pion == 2:
                    for move in self.get_possible_moves_goat(state.board, y, x):
                        if state.board[move[0]][move[1]] == 0:
                            possible.append(GameMove(2, y, x, move[0], move[1]))
        return possible

    def getPossibleGoatPlaces(self, board):
        possibleGoatPlaces = []
        for x in range(5):
            for y in range(5):
                if board[y][x] == 0:
                    possibleGoatPlaces.append(GameMove(2, y, x, y, x))
        return possibleGoatPlaces

    def getPossibleTigerPlaces(self, board):
        possibleTigerPlaces = []
        for x in range(5):
            for y in range(5):
                if board[y][x] == 0 and x > 0 and y > 0 and x < 4 and y < 4:
                    possibleTigerPlaces.append(GameMove(1, y, x, y, x))
        return possibleTigerPlaces

    def checkIfTigersBlocked(self):
        if self.addingTigers == 0:
            for x in range(5):
                for y in range(5):
                    if self.board[y][x] == 1:
                        for neighbour in self.block_checker[x * 5 + y]:
                            if self.board[int(neighbour / 5)][int(neighbour % 5)] == 0:
                                return False
            return True   
        else:
            return False

    def check_status(self):
        if self.checkIfTigersBlocked():
            return 1
        elif self.lostGoats >= 8:
            return -1
        else:
            return 0

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

    def move_tiger(self, state, posY, posX, destY, destX):
        for capture_move in self.capture_connections[posX * 5 + posY]:
            if capture_move == destX * 5 + destY and state.board[destY][destX] == 0 and state.board[int((destY + posY) / 2)][int((destX + posX) / 2)] == 2:
                #zbijanie kozy
                state.board[posY][posX] = 0
                state.board[int((destY + posY) / 2)][int((destX + posX) / 2)] = 0
                state.addedGoats-=1
                state.lostGoats+=1
                state.board[destY][destX] = 1

        for normal_move in self.move_tigers_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and state.board[destY][destX] == 0 and self.checkRoad(state.board, posX, posY, destX, destY) == True: 
                #tylko przesunięcie       
                state.board[posY][posX] = 0
                state.board[destY][destX] = 1
        return state

    def move_goat(self, state, posY, posX, destY, destX):
        for normal_move in self.move_goats_connections[posX * 5 + posY]:
            if normal_move == destX * 5 + destY and state.board[destY][destX] == 0:
                #tylko przesunięcie       
                state.board[posY][posX] = 0
                state.board[destY][destX] = 2
        return state

    def add_tiger(self, state, posY, posX):
        if state.addingTigers > 0:
            #stawianie      
            if state.board[posY][posX] == 0:
                state.board[posY][posX] = 1
                state.addingTigers -= 1
                if state.addingTigers == 0:
                    state.addingGoats = True
                return state, True
        return state, False

    def add_goat(self, state, posY, posX):
        if state.addingGoats == True:
            #stawianie      
            if state.board[posY][posX] == 0:
                state.board[posY][posX] = 2
                state.addedGoats += 1
                state.leftGoats -= 1
                return state, True
        return state, False

    def print(self):
        print("__|0  1  2  3  4")
        for i in range(5):
            print(str(i)+" "+str(self.board[i]))
