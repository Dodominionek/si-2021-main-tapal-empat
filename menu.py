from pvpgame import Board, PVPGame
from pvegame import PVTGame, BVBGame
from tkinter import Widget
import pygame

from pygame.scrap import lost, put

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from tkinter import filedialog

import sys, tkinter

root = tkinter.Tk()
root.withdraw()

class Okno(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(Okno,self).__init__(*args,**kwargs) 
        self.setWindowTitle("Main Tapal Empat")
        self.setFixedWidth(1200)
        self.setFixedHeight(600)

        blankSpace = QLabel()
        blankSpace.setFont(QFont('Impact',32))

        titletext = QLabel()
        titletext.setText("Main Tapal Empat Game")
        titletext.setAlignment(Qt.AlignCenter)
        titletext.setFont(QFont('Impact',32))
        titletext.setStyleSheet("QLabel { color: black; }")

        self.pvpButton = QPushButton()
        self.pvpButton.setText("Player vs Player")
        self.pvpButton.setFont(QFont('Impact',20))
        self.pvpButton.clicked.connect(self.playerVsPlayer)

        self.pvtigerButton = QPushButton()
        self.pvtigerButton.setText("Player vs Tiger Bot")
        self.pvtigerButton.setFont(QFont('Impact',20))
        self.pvtigerButton.clicked.connect(self.playerVsTiger)

        self.bvbButton = QPushButton()
        self.bvbButton.setText("Bot vs Bot")
        self.bvbButton.setFont(QFont('Impact',20))
        self.bvbButton.clicked.connect(self.bvb)

        self.simulationsText = QLabel()
        self.simulationsText.setText("Simulations Number")
        self.simulationsText.setAlignment(Qt.AlignCenter)
        self.simulationsText.setFont(QFont('Impact',20))

        self.simulationsField = QLineEdit()
        self.simulationsField.setText("150")
        self.simulationsField.setFixedWidth(520)
        self.simulationsField.setAlignment(Qt.AlignCenter)
        self.simulationsField.setFont(QFont('Impact',20))

        mainMenu = QVBoxLayout()
        mainMenu.setAlignment(Qt.AlignCenter)
        mainMenu.addWidget(titletext)
        mainMenu.addWidget(blankSpace)
        mainMenu.addWidget(blankSpace)
        mainMenu.addWidget(self.pvpButton)
        mainMenu.addWidget(blankSpace)
        mainMenu.addWidget(self.pvtigerButton)
        mainMenu.addWidget(self.bvbButton)
        mainMenu.addWidget(blankSpace)
        mainMenu.addWidget(self.simulationsText)
        mainMenu.addWidget(self.simulationsField)
        mainMenu.addWidget(blankSpace)
        
        mainMenuW = QWidget()
        mainMenuW.setLayout(mainMenu)

        self.setCentralWidget(mainMenuW)

    def playerVsPlayer(self):
        self.hide()
        pygame.init()
        pygame.font.init()
        pvp = PVPGame(self)

    def playerVsTiger(self):
        self.hide()
        pygame.init()
        pygame.font.init()
        simulations_number = int(self.simulationsField.text())
        pvt = PVTGame(self, simulations_number)

    def bvb(self):
        simulations_number = int(self.simulationsField.text())
        if simulations_number < 150:
            self.simulationsField.setText('')
            self.simulationsField.setPlaceholderText('Minimum 150')
        else:
            self.hide()
            pygame.init()
            pygame.font.init()
            bvb = BVBGame(self, simulations_number)

app = QApplication(sys.argv)

window = Okno()
window.setStyleSheet("background-color: rgb(245,245,220);")
window.show()

app.exec_()