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

def make_move_tiger(board, posY, posX, destY, destX):
    possible_move = False
    for capture_move in capture_connections[posX * 5 + posY]:
        if capture_move == destX * 5 + destY and board[destY][destX] == 0 and board[int((destY + posY) / 2)][int((destX + posX) / 2)] == 2:
            # board[posY][posX] = 0
            # board[int((destY + posY) / 2)][int((destX + posX) / 2)] = 0
            # posX = destX
            # posY = destY
            # board[posY][posX] = 1
            possible_move = True

    for normal_move in move_tigers_connections[posX * 5 + posY]:
        if normal_move == destX * 5 + destY and board[destY][destX] == 0 and checkRoad(board, posX, posY, destX, destY) == True:
            # board[posY][posX] = 0
            # posX = destX
            # posY = destY
            # board[posY][posX] = 1
            possible_move = True

    return possible_move

def checkRoad(board, tigerX, tigerY, destX, destY):
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

def make_move_goat(board, posY, posX, destY, destX):
    possible_move = False
    for normal_move in move_goats_connections[posX * 5 + posY]:
        if normal_move == destX * 5 + destY and board[destY][destX] == 0:
            # board[posY][posX] = 0
            # posX = destX
            # posY = destY
            # board[posY][posX] = 2
            possible_move = True
    return possible_move

board = [
    [0,1,0,0,0],
    [0,1,2,0,0],
    [0,2,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

def get_possible_moves_tiger(board, posX, posY):
    possible = []
    for x in range(5):
        for y in range(5):
            if make_move_tiger(board, posX, posY, x, y) == True:
                possible.append([x, y])
    return possible

def get_possible_moves_goat(board, posX, posY):
    possible = []
    for x in range(5):
        for y in range(5):
            if make_move_goat(board, posX, posY, x, y) == True:
                possible.append([x, y])
    return possible

print(get_possible_moves_tiger(board, 0, 1))

print(get_possible_moves_goat(board, 1, 2))


# for row in board:
#     print(row)

# # plansza, numer wiersza zwierzęcia, numer kolumny zwierzęcia, numer wiersza docelowy, numer kolumny docelowy, liczone od 0
# make_move_tiger(board, 0, 1, 0, 3)

# print()
# for row in board:
#     print(row)
    
# make_move_tiger(board, 1, 1, 3, 1)

# print()
# for row in board:
#     print(row)

# make_move_goat(board, 1, 2, 1, 0)

# print()
# for row in board:
#     print(row)