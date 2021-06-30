from copy import Error, error
from tkinter import Widget
from numpy import ubyte, who
import pygame
import math
from mcts.nodes import *
from mcts.search import MonteCarloTreeSearch
from pygame.scrap import lost, put
from game import *
from state import *
from tkinter import Widget
import pygame
import math
from pygame.scrap import lost, put
import threading

running = None
myfont = None

def init(sim_count, board, screen):
    state = State()
    initial_board_state = GameState(state=state, next_to_move=1)

    state.print()
    root = MonteCarloTreeSearchNode(state=initial_board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)

    best_node = mcts.best_action(sim_count)
    c_state = best_node.state
    state_copy = c_state.state

    updateScreen(c_state.state.board, board, screen)
    pygame.display.flip()

    board_state = GameState(state=state_copy, next_to_move=1)
    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
    mcts = MonteCarloTreeSearch(root)
    best_node = mcts.best_action(sim_count)
    c_state = best_node.state

    return c_state

def get_action(state, screen):
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x = x + 50
                y = y + 50
                if x > 100 and x < 1100 and y > 100 and y < 1100:
                    xToDraw = x
                    yToDraw = y
                    x = math.floor(x / 200)
                    y = math.floor(y / 200)
                    if state.state.addingGoats:
                        if state.state.board[y][x] == 0:
                            move = GameMove(2, y, x, y, x)
                        else:
                            raise(Exception)
                    else:
                        if state.state.board[y][x] == 2:
                            pygame.draw.circle(screen, 'green', [math.floor(xToDraw / 100) * 100, math.floor(yToDraw / 100) * 100], 30)
                            pygame.draw.circle(screen, 'gray', [math.floor(xToDraw / 100) * 100, math.floor(yToDraw / 100) * 100], 28)
                            pygame.display.flip()
                            noCoords = True
                            while noCoords:
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        xTo, yTo = pygame.mouse.get_pos()
                                        xTo = xTo + 50
                                        yTo = yTo + 50
                                        if xTo > 100 and xTo < 1100 and yTo > 100 and yTo < 1100:
                                            xTo = math.floor(xTo / 200)
                                            yTo = math.floor(yTo / 200)
                                            if state.state.board[yTo][xTo] == 0:
                                                pygame.draw.circle(screen, 'gray', [math.floor(xToDraw / 100) * 100, math.floor(yToDraw / 100) * 100], 30)
                                                move = GameMove(2, y, x, yTo, xTo)
                                                noCoords = False
                                            else:
                                                raise(Exception)
                                        else:
                                            raise(Exception)
                        else:
                            raise(Exception)
    except Exception as e:
        move = -1
    if move == -1:
        print("invalid move")
        move = get_action(state)
    return move


def judge(state):
    if state.is_game_over() != None:
        if state.game_result == 1.0:
            print("You lose!")
        if state.game_result == -1.0:
            print("You Win!")
        return 1
    else:
        return -1

empty = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
] 

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

def clearText(screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost):
    bigfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = bigfont.render(text, False, (255, 255, 255))
    screen.blit(textsurface,(1000,450))
    textGoatsLeftSurface = myfont.render(textGoatsLeft, False, (255, 255, 255))
    screen.blit(textGoatsLeftSurface,(1000,100))
    textGoatsDeployedSurface = myfont.render(textGoatsDeployed, False, (255, 255, 255))
    screen.blit(textGoatsDeployedSurface,(1000,150))
    textGoatsSurface = myfont.render(textGoats, False, (255, 255, 255))
    screen.blit(textGoatsSurface,(1000,200))
    textGoatsLostSurface = myfont.render(textGoatsLost, False, (255, 255, 255))
    screen.blit(textGoatsLostSurface,(1000,250))

def writeText(screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost):
    bigfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = bigfont.render(text, False, (0, 0, 0))
    screen.blit(textsurface,(1000,450))
    textGoatsLeftSurface = myfont.render(textGoatsLeft, False, (0, 0, 0))
    screen.blit(textGoatsLeftSurface,(1000,100))
    textGoatsDeployedSurface = myfont.render(textGoatsDeployed, False, (0, 0, 0))
    screen.blit(textGoatsDeployedSurface,(1000,150))
    textGoatsSurface = myfont.render(textGoats, False, (0, 0, 0))
    screen.blit(textGoatsSurface,(1000,200))
    textGoatsLostSurface = myfont.render(textGoatsLost, False, (0, 0, 0))
    screen.blit(textGoatsLostSurface,(1000,250))

def updateScreen(board_c_state, board, screen):
    board.prepareBoard(screen)
    for x in range(5):
        for y in range(5):
            if board_c_state[y][x] == 1:
                pygame.draw.circle(screen, 'orange', [x * 200 + 100, y * 200 + 100], 30)
            elif board_c_state[y][x] == 2:
                pygame.draw.circle(screen, 'grey', [x * 200 + 100, y * 200 + 100], 30)
            else:
                pygame.draw.circle(screen, 'black', [x * 200 + 100, y * 200 + 100], 30)

class PVTGame():
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

    def mctsBestNode(self, mcts, sim_count):
        self.best_node = mcts.best_action(sim_count)

    def initialise(self, sim_count):
        self.initState = init(sim_count, self.board, self.screen)

    def __init__(self, menu, sim_count):
        self.menu = menu
        self.best_node = None
        self.screen = pygame.display.set_mode([1500, 1000])
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.board = Board()
        text = 'Tygrysy rozstawiają'
        self.running = True
        self.screen.fill((255, 255, 255))
        self.board.prepareBoard(self.screen)
        textGoatsLeft = 'Pozostałe kozy: ' + str(18)
        textGoatsDeployed = 'Rozstawione kozy: ' + str(0)
        textGoats = 'Kozy na planszy: ' + str(0)
        textGoatsLost  = 'Utracone kozy: ' + str(0)
        clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
        writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
        pygame.display.flip()
        self.quit = True
        self.initState = None
        init_thread = threading.Thread(target=self.initialise, args = [sim_count])
        init_thread.start()
        while init_thread.is_alive() and self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    text = 'Zamykanie'
                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    pygame.display.flip()
                    init_thread.join()
                    pygame.quit()
                    self.menu.show()
                    self.quit = False
        if self.quit == True:
            c_state = self.initState
            c_state.state.print()
            clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
            text = 'Ruch kóz'
            updateScreen(c_state.state.board, self.board, self.screen)
            writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
            pygame.display.flip()

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                updateScreen(c_state.state.board, self.board, self.screen)
                pygame.display.flip()
                check = True
                while check == True:
                    check = False
                    try:
                        move1 = get_action(c_state, self.screen)
                        c_state = c_state.move(move1)
                    except:
                        check = True
                c_state.state.print()
                updateScreen(c_state.state.board, self.board, self.screen)
                pygame.display.flip()
                
                if judge(c_state) == 1:
                    break

                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Ruch tygrysów'
                textGoatsLeft = 'Pozostałe kozy: ' + str(c_state.state.leftGoats)
                textGoatsDeployed = 'Rozstawione kozy: ' + str(c_state.state.addedGoats)
                textGoats = 'Kozy na planszy: ' + str(c_state.state.addedGoats - c_state.state.lostGoats)
                textGoatsLost  = 'Utracone kozy: ' + str(c_state.state.lostGoats)
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                pygame.display.flip()

                state_copy = c_state.state

                board_state = GameState(state=state_copy, next_to_move=1)
                root = MonteCarloTreeSearchNode(state=board_state, parent=None)
                mcts = MonteCarloTreeSearch(root)

                # best_node = mcts.best_action(sim_count)
                sim_thread = threading.Thread(target=self.mctsBestNode, args = (mcts, sim_count))
                sim_thread.start()
                while sim_thread.is_alive() and self.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                            text = 'Zamykanie'
                            writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                            pygame.display.flip()
                            sim_thread.join()
                            self.running = False
                            pygame.quit()
                            self.menu.show()

                if self.running == True:
                    c_state = self.best_node.state
                    c_state.state.print()
                    updateScreen(c_state.state.board, self.board, self.screen)
                    pygame.display.flip()

                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    text = 'Ruch kóz'
                    textGoatsLeft = 'Pozostałe kozy: ' + str(c_state.state.leftGoats)
                    textGoatsDeployed = 'Rozstawione kozy: ' + str(c_state.state.addedGoats)
                    textGoats = 'Kozy na planszy: ' + str(c_state.state.addedGoats - c_state.state.lostGoats)
                    textGoatsLost  = 'Utracone kozy: ' + str(c_state.state.lostGoats)
                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    pygame.display.flip()
                    
                    if judge(c_state)==1:
                        break
                    elif judge(c_state)==-1:
                        continue

                    pygame.display.flip()

            if c_state.state.check_status() == -1:
                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Kozy wygraly'
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                pygame.display.flip()
            elif c_state.state.check_status() == 1:
                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Tygrysy wygraly'
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                pygame.display.flip()
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        self.menu.show()


class BVBGame():
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

    def mctsBestNode(self, mcts, sim_count):
        self.best_node = mcts.best_action(sim_count)

    def initialise(self, sim_count):
        self.initState = init(sim_count, self.board, self.screen)

    def __init__(self, menu, sim_count):
        self.menu = menu
        self.best_node = None
        self.screen = pygame.display.set_mode([1500, 1000])
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.board = Board()
        text = 'Tygrysy rozstawiają'
        self.running = True
        self.screen.fill((255, 255, 255))
        self.board.prepareBoard(self.screen)
        textGoatsLeft = 'Pozostałe kozy: ' + str(18)
        textGoatsDeployed = 'Rozstawione kozy: ' + str(0)
        textGoats = 'Kozy na planszy: ' + str(0)
        textGoatsLost  = 'Utracone kozy: ' + str(0)
        clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
        writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
        pygame.display.flip()
        self.quit = True
        self.initState = None
        init_thread = threading.Thread(target=self.initialise, args = [sim_count])
        init_thread.start()
        while init_thread.is_alive() and self.quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    text = 'Zamykanie'
                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    pygame.display.flip()
                    init_thread.join()
                    pygame.quit()
                    self.menu.show()
                    self.quit = False
        if self.quit == True:
            c_state = self.initState
            c_state.state.print()

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False

                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Ruch kóz'
                textGoatsLeft = 'Pozostałe kozy: ' + str(c_state.state.leftGoats)
                textGoatsDeployed = 'Rozstawione kozy: ' + str(18 - c_state.state.leftGoats)
                textGoats = 'Kozy na planszy: ' + str(18 - c_state.state.leftGoats - c_state.state.lostGoats)
                textGoatsLost  = 'Utracone kozy: ' + str(c_state.state.lostGoats)
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                updateScreen(c_state.state.board, self.board, self.screen)
                pygame.display.flip()

                state_copy = c_state.state

                board_state = GameState(state=state_copy, next_to_move=-1)
                root = MonteCarloTreeSearchNode(state=board_state, parent=None)
                mcts = MonteCarloTreeSearch(root)

                sim_thread = threading.Thread(target=self.mctsBestNode, args = (mcts, sim_count))
                sim_thread.start()
                while sim_thread.is_alive() and self.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                            text = 'Zamykanie'
                            writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                            pygame.display.flip()
                            sim_thread.join()
                            self.running = False
                            pygame.quit()
                            self.menu.show()

                if self.running == True:
                # best_node = mcts.best_action(sim_count)
                    c_state = self.best_node.state
                    c_state.state.print()
                    updateScreen(c_state.state.board, self.board, self.screen)
                    pygame.display.flip()

                    if judge(c_state)==1:
                        break

                    clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    text = 'Ruch tygrysów'
                    textGoatsLeft = 'Pozostałe kozy: ' + str(c_state.state.leftGoats)
                    textGoatsDeployed = 'Rozstawione kozy: ' + str(18 - c_state.state.leftGoats)
                    textGoats = 'Kozy na planszy: ' + str(18 - c_state.state.leftGoats - c_state.state.lostGoats)
                    textGoatsLost  = 'Utracone kozy: ' + str(c_state.state.lostGoats)
                    writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                    pygame.display.flip()

                    state_copy = c_state.state

                    board_state = GameState(state=state_copy, next_to_move=1)
                    root = MonteCarloTreeSearchNode(state=board_state, parent=None)
                    mcts = MonteCarloTreeSearch(root)

                    sim_thread = threading.Thread(target=self.mctsBestNode, args = (mcts, sim_count))
                    sim_thread.start()
                    while sim_thread.is_alive() and self.running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                                text = 'Zamykanie'
                                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                                pygame.display.flip()
                                sim_thread.join()
                                self.running = False
                                pygame.quit()
                                self.menu.show()

                    if self.running == True:
                    # best_node = mcts.best_action(sim_count)
                        c_state = self.best_node.state
                        c_state.state.print()
                        updateScreen(c_state.state.board, self.board, self.screen)
                        pygame.display.flip()
                        
                        if judge(c_state)==1:
                            break
                        elif judge(c_state)==-1:
                            continue

                        pygame.display.flip()

            if c_state.state.check_status() == -1:
                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Kozy wygraly'
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                pygame.display.flip()
            elif c_state.state.check_status() == 1:
                clearText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                text = 'Tygrysy wygraly'
                writeText(self.screen, myfont, text, textGoatsLeft, textGoatsDeployed, textGoats, textGoatsLost)
                pygame.display.flip()
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        self.menu.show()
                