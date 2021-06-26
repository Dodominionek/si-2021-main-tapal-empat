from copy import Error
import math
import numpy as np
from collections import defaultdict
from state import GameState
from game import *

class Node:

    def __init__(self, state: GameState, parent = None):
        self.node_state = state
        self.parent = parent
        self.children = []
        self.visits_number = 0
        self.results = defaultdict(int)

    def is_last_node(self):
        return self.node_state.is_game_over()

    @property
    def untried_actions(self):
        if not hasattr(self, '_untried_actions'):
            self._untried_actions = self.node_state.get_legal_actions()
        return self._untried_actions

    @property
    def q(self):
        wins = self.results[self.parent.node_state.next_to_move]
        loses = self.results[self.parent.node_state.next_to_move]
        return wins - loses

    @property
    def n(self):
        return self.visits_number

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.node_state.move(action)
        child_node = Node(next_state, parent = self)
        self.children.append(child_node)
        return child_node

    def rollout(self):
        current_rollout_state = self.node_state
        while current_rollout_state.is_game_over() != 1 or current_rollout_state.is_game_over() != 2 and current_rollout_state.state.addingTigers != 0:
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result

    def backpropagate(self, result):
        self.visits_number += 1.
        self.results[result] += 1.
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
        print(possible)
        return possible_moves[np.random.randint(possible)]
