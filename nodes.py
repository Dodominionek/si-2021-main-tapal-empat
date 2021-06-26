import numpy as np
from numpy.lib import math

class MCTSTreeNode:

    def __init__(self, state, parent):
        self.parent = parent
        self.children = []
        self.score = 0
        self.number_of_visits = 0
        self.node_state = state
        self.results = []
        self.possible_moves = self.node_state.get_legal_actions()
        self.tiger_wins = 0
        self.goat_wins = 0


    # Sprawdza czy gra się kńczy
    def is_terminal_node(self):
        return self.node_state.is_game_over()

    # Badanie ruchu
    def explore(self):
        current_state = self.node_state
        # Dopóki nie dojdzie do ruchu końcowego wykonuje randomowe operacje
        # Po ruchu usuwa go z listy dostępnych
        while current_state.is_terminal_node() == None:
            choice = np.random.randint(len(self.possible_moves))
            move_choice = self.possible_moves[choice]
            self.possible_moves.pop(choice)
            current_state = current_state.move(move_choice)
        return current_state.game_result

    # Zwiększa listę gałęzi
    def expand(self):
        new_state = self.possible_moves.pop()
        child = MCTSTreeNode(new_state, parent = self)
        self.children.append(child)
        return child

    # Sprawdza czy wybrał wszystkie opcje
    def is_fully_expanded(self):
        return len(self.possible_moves) == 0

    # Wybiera najlepszą gałąź
    def best_child(self, c_param = 1.4):
        best_child = self.children[0]
        for child in self.children:
            res = (self.tiger_wins - self.goat_wins) / float(self.number_of_visits) + c_param * math.sqrt(2*float(math.log(self.number_of_visits) / float(self.number_of_visits)))
            child.score = res
            if best_child.score < child.score:
                best_child = child
        return best_child

    # Zlicza wygrane i przegrane
    def count_victories_loses(self, tiger_wins, goat_wins):
        self.number_of_visits += 1.
        if self.node_state.is_game_over() == 1:
            self.tiger_wins += tiger_wins + 1
        if self.node_state.is_game_over() == 2:
            self.goat_wins += goat_wins + 1
        if self.parent:
            self.parent.backpropagate(self.tiger_wins, self.goat_wins)
            