from tkinter import Widget
import pygame
import math

from pygame.scrap import lost, put

empty = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
] 

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

class Board:
    def __init__(self):
        self.tigers = []
        self.goats = []
        self.fieldsRows = []
        self.fields = empty

    def prepareBoard(self, screen):
        for z in range(5):
            pygame.draw.lines(screen, 'black', False, [(100, 100 + (z * 200)), (900, 100 + (z * 200))], 5)
            pygame.draw.lines(screen, 'black', False, [(100 + (z * 200), 100), (100 + (z * 200), 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 100), (900, 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(500, 100), (900, 500)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 500), (500, 900)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 900), (900, 100)], 5)
        pygame.draw.lines(screen, 'black', False, [(100, 500), (500, 100)], 5)
        pygame.draw.lines(screen, 'black', False, [(500, 900), (900, 500)], 5)
        for x in range(5):
            row = []
            for y in range(5):
                field = Field(x * 200, y * 200, (x + 1) * 200, (y + 1) * 200, x * 5 + y, screen)
                row.append(field)
            self.fieldsRows.append(row)

    def updateBoard(self, screen):
        self.fields = empty
        for tiger in self.tigers:
            pygame.draw.circle(screen, 'orange', [tiger.x, tiger.y], 30)
            self.fields[math.floor(tiger.y / 200)][math.floor(tiger.x / 200)] = 1
        for goat in self.goats:
            pygame.draw.circle(screen, 'grey', [goat.x, goat.y], 30)
            self.fields[math.floor(goat.y / 200)][math.floor(goat.x / 200)] = 2

class Field:
    def __init__(self, xStart, yStart, xEnd, yEnd, id, screen):
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.id = id
        self.color = 'black'
        self.drawField(screen)
    
    def drawField(self, screen):
        center = [(self.xStart + self.xEnd) / 2, (self.yStart + self.yEnd) / 2]
        pygame.draw.circle(screen, self.color, center, 30)

    def changeColor(self, col):
        self.color = col

# pygame.init()
# pygame.font.init()
# myfont = pygame.font.SysFont('Comic Sans MS', 30)

# screen = pygame.display.set_mode([1500, 1000])

# board = Board()

# text = 'Tygrysy rozstawiają'

# color = 'orange'
# addingTigers = True
# addingGoats = False
# tigersMove = False
# addedGoats = 0
# leftGoats = 18
# lostGoats = 0

# ended = False

# textGoatsLeft = 'Pozostałe kozy: ' + str(leftGoats - addedGoats)

# textGoatsDeployed = 'Wykorzystane kozy: ' + str(addedGoats)

# textGoats = 'Kozy na planszy: ' +  str(len(board.goats))

# textGoatsLost = 'Stracone kozy: ' + str(addedGoats - len(board.goats))

def checkRoad(destX, destY, tigerX, tigerY, board):
    tempX = destX
    tempY = destY
    while tempX != tigerX or tempY != tigerY:
        if board.fields[math.floor(tempY / 200)][math.floor(tempX / 200)] == 1:
            return False
        if destY == tigerY and destX > tigerX:
            tempX = tempX - 200
        elif destY == tigerY and destX < tigerX:
            tempX = tempX + 200
        elif destX == tigerX and destY < tigerY:
            tempY = tempY + 200
        elif destX == tigerX and destY > tigerY:
            tempY = tempY - 200
        elif destX > tigerX and destY > tigerY:
            tempX = tempX - 200
            tempY = tempY - 200
        elif destX < tigerX and destY > tigerY:
            tempX = tempX + 200
            tempY = tempY - 200
        elif destX > tigerX and destY < tigerY:
            tempX = tempX - 200
            tempY = tempY + 200
        elif destX < tigerX and destY < tigerY:
            tempX = tempX + 200
            tempY = tempY + 200
        if board.fields[math.floor(tempY / 200)][math.floor(tempX / 200)] == 2:
            return False
    return True

class Tiger:
    def __init__(self, x, y):
        self.isBlocked = False
        self.x = x
        self.y = y

    def makeMove(self, tigerX, tigerY, board, screen):
        noCoords = True
        while noCoords:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseX = mouseX + 50
                    mouseY = mouseY + 50

                    destX = math.floor((mouseX) / 100) * 100
                    destY = math.floor((mouseY) / 100) * 100
                    # Sprawdza połączenia
                    for connection in move_tigers_connections[math.floor(tigerX / 200) * 5 + math.floor(tigerY / 200)]:
                        if connection == math.floor(mouseX / 200) * 5 + math.floor(mouseY / 200) and board.fields[math.floor(destY / 200)][math.floor(destX / 200)] == 0 and (destX % 200 != 0 and destY % 200 != 0):
                            if checkRoad(destX, destY, tigerX, tigerY, board) == True:
                                for tiger in board.tigers:
                                    if tiger.x == tigerX and tiger.y == tigerY:
                                        board.fields[math.floor(tigerY / 200)][math.floor(tigerX / 200)] = 0
                                        tiger.x = destX
                                        tiger.y = destY
                                        pygame.draw.circle(screen, 'black', [tigerX, tigerY], 30)
                                noCoords = False   
                    for cap_connection in capture_connections[math.floor(tigerX / 200) * 5 + math.floor(tigerY / 200)]:
                        if cap_connection == math.floor(mouseX / 200) * 5 + math.floor(mouseY / 200) and board.fields[math.floor(destY / 200)][math.floor(destX / 200)] == 0 and (destX % 200 != 0 and destY % 200 != 0):
                            if board.fields[math.floor((destY + tigerY) / 2 / 200)][math.floor((destX + tigerX) / 2 / 200)] == 2:
                                for tiger in board.tigers:
                                    if tiger.x == tigerX and tiger.y == tigerY:
                                        pygame.draw.circle(screen, 'black', [tigerX, tigerY], 30)
                                        pygame.draw.circle(screen, 'black', [math.floor((destX + tigerX) / 2), math.floor((destY + tigerY) / 2)], 30)
                                        board.fields[math.floor(tigerY / 200)][math.floor(tigerX / 200)] = 0
                                        board.fields[math.floor((destY + tigerY) / 2 / 200)][math.floor((destX + tigerX) / 2 / 200)] = 0
                                        print(board.fields[math.floor((destY + tigerY) / 2 / 200)][math.floor((destX + tigerX) / 2 / 200)])
                                        tiger.x = destX
                                        tiger.y = destY
                                        for goat in board.goats:
                                            if goat.x == math.floor((destX + tigerX) / 2) and goat.y == math.floor((destY + tigerY) / 2):
                                                board.goats.remove(goat)
                                noCoords = False   

class Goat:
    def __init__(self, x, y):
        self.isAlive = True
        self.x = x
        self.y = y

    def makeMove(self, goatX, goatY, board, screen):
        noCoords = True
        while noCoords:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseX = mouseX + 50
                    mouseY = mouseY + 50

                    destX = math.floor(mouseX / 100) * 100
                    destY = math.floor(mouseY / 100) * 100
                    for connection in move_goats_connections[math.floor(goatX / 200) * 5 + math.floor(goatY / 200)]:
                        if connection == math.floor(mouseX / 200) * 5 + math.floor(mouseY / 200) and board.fields[math.floor(destY / 200)][math.floor(destX / 200)] == 0 and (destX % 200 != 0 and destY % 200 != 0):
                            for goat in board.goats:
                                if goat.x == goatX and goat.y == goatY:
                                    board.fields[math.floor(goatY / 200)][math.floor(goatX / 200)] = 0
                                    goat.x = destX
                                    goat.y = destY
                                    pygame.draw.circle(screen, 'black', [goatX, goatY], 30)
                            noCoords = False


# running = True

# screen.fill((255, 255, 255))
# board.prepareBoard()

def isInsideSquare(x, y):
    if math.floor(x / 100) * 100 >= 300 and math.floor(x / 100) * 100 <= 700 and math.floor(y / 100) * 100 >= 300 and math.floor(y / 100) * 100 <= 700:
        return True
    else:
        return False

def goatLost(goatX, goatY, board):
    for goat in board.goats:
        if goat.x == goatX and goat.y == goatY:
            board.goats.remove(goat)
            board.fields[goat.x][goat.y] = 0

def checkIfTigersBlocked(board):
    for tiger in board.tigers:
        for neigbour in block_checker[math.floor(tiger.y / 200) * 5 + math.floor(tiger.x / 200)]:
            if board.fields[math.floor(neigbour / 5)][neigbour % 5] == 0:
                return False
    return True   

def clearText(screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost):
    textsurface = myfont.render(text, False, (255, 255, 255))
    screen.blit(textsurface,(0,0))
    textGoatsLeftSurface = myfont.render(textGoatsLeft, False, (255, 255, 255))
    screen.blit(textGoatsLeftSurface,(1000,0))
    textGoatsDeployedSurface = myfont.render(textGoatsDeployed, False, (255, 255, 255))
    screen.blit(textGoatsDeployedSurface,(1000,50))
    textGoatsSurface = myfont.render(textGoats, False, (255, 255, 255))
    screen.blit(textGoatsSurface,(1000,100))
    textGoatsLostSurface = myfont.render(textGoatsLost, False, (255, 255, 255))
    screen.blit(textGoatsLostSurface,(1000,150))

def writeText(screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost):
    textsurface = myfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))
    textGoatsLeftSurface = myfont.render(textGoatsLeft, False, (0, 0, 0))
    screen.blit(textGoatsLeftSurface,(1000,0))
    textGoatsDeployedSurface = myfont.render(textGoatsDeployed, False, (0, 0, 0))
    screen.blit(textGoatsDeployedSurface,(1000,50))
    textGoatsSurface = myfont.render(textGoats, False, (0, 0, 0))
    screen.blit(textGoatsSurface,(1000,100))
    textGoatsLostSurface = myfont.render(textGoatsLost, False, (0, 0, 0))
    screen.blit(textGoatsLostSurface,(1000,150))

class PVPGame():
    global text
    global textGoats
    global textGoatsDeployed
    global textGoatsLost
    global textGoatsLeft
    global running
    global ended
    global screen
    global myfont
    global board
    global addedGoats
    global leftGoats

    def __init__(self, menu):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = pygame.display.set_mode([1500, 1000])
        self.board = Board()
        text = 'Tygrysy rozstawiają'
        color = 'orange'
        addingTigers = True
        addingGoats = False
        tigersMove = False
        addedGoats = 0
        leftGoats = 18
        lostGoats = 0
        ended = False
        textGoatsLeft = 'Pozostałe kozy: ' + str(leftGoats - addedGoats)
        textGoatsDeployed = 'Wykorzystane kozy: ' + str(addedGoats)
        textGoats = 'Kozy na planszy: ' +  str(len(self.board.goats))
        textGoatsLost = 'Stracone kozy: ' + str(addedGoats - len(self.board.goats))
        running = True
        self.screen.fill((255, 255, 255))
        self.board.prepareBoard(self.screen)

        while running:
            writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)

            for event in pygame.event.get():
                if (len(self.board.tigers) >= 2):
                    addingTigers = False
                    color = 'grey'
                    if addedGoats >= 18:
                        addingGoats = False
                    else:
                        addingGoats = True

                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)

                    x, y = pygame.mouse.get_pos()
                    x = x + 50
                    y = y + 50
                    if x > 100 and x < 1100 and y > 100 and y < 1100 and not ended:
                        if (math.floor(x / 100) * 100) % 200 != 0 and (math.floor(y / 100) * 100) % 200 != 0:
                            for row in self.board.fieldsRows:
                                for field in row:
                                    if (field.xStart + field.xEnd) / 2 == math.floor(x / 100) * 100 and (field.yStart + field.yEnd) / 2 == math.floor(y / 100) * 100:
                                        if addingTigers == True and isInsideSquare(x, y) and self.board.fields[math.floor(y / 200)][math.floor(x / 200)] == 0:
                                            print('Tygrysy rozstawiły')
                                            text = 'Tygrysy rozstawiły ' + str(len(self.board.tigers) + 1)
                                            self.board.tigers.append(Tiger(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
                                            pygame.draw.circle(self.screen, color, [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                        elif tigersMove == True:
                                            for tiger in self.board.tigers:
                                                if math.floor(x / 100) * 100 == tiger.x and math.floor(y / 100) * 100 == tiger.y:
                                                    pygame.draw.circle(self.screen, 'green', [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                                    pygame.draw.circle(self.screen, 'orange', [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 28)
                                                    
                                                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                                                    pygame.display.flip()
                                                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)

                                                    tiger.makeMove(tiger.x, tiger.y, self.board, self.screen)
                                                    print('Tygrysy zrobiły ruch')
                                                    text = 'Tygrysy zrobiły ruch'
                                                    tigersMove = False
                                        elif addingGoats == True and self.board.fields[math.floor(y / 200)][math.floor(x / 200)] == 0:
                                            print('Kozy rozstawiły')
                                            text = 'Kozy rozstawiły '
                                            self.board.goats.append(Goat(math.floor(x / 100) * 100, math.floor(y / 100) * 100))
                                            pygame.draw.circle(self.screen, color, [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                            if len(self.board.goats) >= 1 :
                                                tigersMove = True
                                            if addedGoats == 18:
                                                addingGoats = False
                                            addedGoats += 1
                                        elif tigersMove == False and addingTigers == False and addingGoats == False:
                                            for goat in self.board.goats:
                                                if math.floor(x / 100) * 100 == goat.x and math.floor(y / 100) * 100 == goat.y:
                                                    pygame.draw.circle(self.screen, 'green', [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 30)
                                                    pygame.draw.circle(self.screen, 'gray', [math.floor(x / 100) * 100, math.floor(y / 100) * 100], 28)
                                                    
                                                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                                                    pygame.display.flip()
                                                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)

                                                    goat.makeMove(goat.x, goat.y, self.board, self.screen)
                                                    print('Kozy zrobiły ruch')
                                                    text = 'Kozy zrobiły ruch'
                                                    tigersMove = True
                        self.board.updateBoard(self.screen)
                        for row in self.board.fields:
                            print(row)
                    textGoats = 'Kozy na planszy: ' +  str(len(self.board.goats))
                    textGoatsDeployed = 'Wykorzystane kozy: ' + str(addedGoats)
                    textGoatsLost = 'Stracone kozy: ' + str(addedGoats - len(self.board.goats))
                    textGoatsLeft = 'Pozostałe kozy: ' + str(leftGoats - addedGoats)
                    if (addedGoats - len(self.board.goats)) >= 8:
                        text = 'Tygrysy wygraly!'
                        ended = True
                    if checkIfTigersBlocked(self.board) == True and len(self.board.tigers) == 2:
                        text = 'Kozy wygraly!'
                        ended = True

            pygame.display.flip()

        pygame.quit()
        menu.show()