from mcts.nodes import Node

class MonteCarloTreeSearch:
    def __init__(self, node: Node):
        self.root = node
        self.last_state = None

    def best_action(self, simulations_number, que=None):
        for _ in range(0, simulations_number):
            v = self.tree_policy()
            try:
                reward = v.rollout()
            except:
                reward = self.last_state.rollout()
            v.backpropagate(reward)
        self.last_state = self.root.best_child()
        return self.root.best_child(c_param=0.)

    def tree_policy(self):
        current_node = self.root
        try:
            while current_node.is_last_node() == 0:
                if not current_node.is_fully_expanded():
                    return current_node.expand()
                else:
                    current_node = current_node.best_child()
        except:
            current_node = self.last_state
        return current_node































# class MonteCarloTreeSearch:
#     def __init__(self, node: MonteCarloTreeSearchNode):
#         self.root = node

#     def best_action(self, simulations_number, que=None):
#         for _ in range(0, simulations_number):
#             v = self.tree_policy()
#             reward = v.rollout()
#             v.backpropagate(reward)
#         return self.root.best_child(c_param=0.)

#     def tree_policy(self):
#         current_node = self.root
#         while not current_node.is_terminal_node():
#             if not current_node.is_fully_expanded():
#                 return current_node.expand()
#             else:
#                 current_node = current_node.best_child()
#         return current_node
