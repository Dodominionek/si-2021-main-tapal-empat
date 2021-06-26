import nodes

class MonteCarloTreeSearch:

    def __init__(self, node):
        self.root = node

    def best_move(self, simulations_number):
        for i in range(0, simulations_number):
            check = self.tree_check()
            reward = check.explore()
            check.count_victories_loses(check.tiger_wins, check.goat_wins)

        best = self.root.best_child(1.4)
        return best

    def tree_check(self):
        current_root = self.root
        while current_root.is_terminal_node() == None:
            if not current_root.is_fully_expanded():
                return current_root.expand()
            else:
                current_root = current_root.best_child()
        return current_root