from mcts.nodes import MonteCarloTreeSearchNode


class MonteCarloTreeSearch:
    def __init__(self, node: MonteCarloTreeSearchNode):
        self.root = node

    def best_action(self, simulations_number):

        # print("Inside best action")
        for _ in range(0, simulations_number):

            # print("Call tree policy")
            v = self.tree_policy()

            # print(v.state.state.board)
            
            # print("Call rollout")
            reward = v.rollout()

            # print("Call backpropagate")
            v.backpropagate(reward)
        # exploitation only
        return self.root.best_child(c_param=0.)

    def tree_policy(self):
        current_node = self.root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                # print("Call expand")
                return current_node.expand()
            else:
                # print("Call best child")
                current_node = current_node.best_child()
        return current_node
