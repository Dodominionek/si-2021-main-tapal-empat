from copy import Error
import math
import numpy as np
import random
from collections import defaultdict
from state import GameState
from game import *

class MonteCarloTreeSearchNode(object):
    def __init__(self, state: GameState, parent=None):
        self._number_of_visits = 0.
        self._results = defaultdict(int)
        self.state = state
        self.parent = parent
        self.children = []
        self.score = 0

    @property
    def untried_actions(self):
        if not hasattr(self, '_untried_actions'):
            self._untried_actions = self.state.get_legal_actions()
            random.shuffle(self._untried_actions)
        return self._untried_actions

    @property
    def q(self):
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1 * self.parent.state.next_to_move]
        return wins - loses

    @property
    def n(self):
        return self._number_of_visits

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MonteCarloTreeSearchNode(next_state, parent=self)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def rollout(self):
        current_rollout_state = self.state
        while current_rollout_state.is_game_over() == None and self.is_fully_expanded() == False and len(current_rollout_state.get_legal_actions()) != 0:
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result

    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=1.4):
        try:
            if len(self.children) == 0:
                raise(Error)
            best = self.children[0]
            for c in self.children:
                s = (c.q / float(c.n)) + c_param * math.sqrt((2 * float(math.log(self.n)) / float(c.n)))
                c.score = s
                if best.score < c.score:
                    best = c
            return best
        except Error as e:
            print(e)


    def rollout_policy(self, possible_moves):
        possible = len(possible_moves)
        return possible_moves[np.random.randint(possible)]
