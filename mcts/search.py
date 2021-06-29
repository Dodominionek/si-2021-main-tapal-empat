from mcts.nodes import MonteCarloTreeSearchNode


class MonteCarloTreeSearch:
    def __init__(self, node: MonteCarloTreeSearchNode):
        self.root = node

    def best_action(self, simulations_number):
        for _ in range(0, simulations_number):
            if self.root != None:
                v = self.tree_policy()
                if v != None:
                    reward = v.rollout()
                    v.backpropagate(reward)
        return self.root.best_child(c_param=0.)

    def tree_policy(self):
        current_node = self.root
        while current_node.is_terminal_node() == None:
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
            if current_node == None:
                break
        return current_node

