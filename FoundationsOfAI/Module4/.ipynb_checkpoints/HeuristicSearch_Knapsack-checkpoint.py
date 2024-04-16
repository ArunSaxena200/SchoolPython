from simpleai.search import SearchProblem, astar

class KnapsackProblem(SearchProblem):
    def __init__(self, items, capacity):
        super().__init__(tuple(items))
        self.capacity = capacity

    def actions(self, state):
        # Generate all possible actions (adding an item to the knapsack)
        return [item for item in state]

    def result(self, state, action):
        # Execute an action and return the new state
        new_state = list(state)
        new_state.remove(action)
        return tuple(new_state)

    def is_goal(self, state):
        # Check if the knapsack cannot accommodate any more items
        return sum(item[1] for item in state) <= self.capacity

    def heuristic(self, state):
        # Heuristic function: estimate the maximum value achievable from the current state
        remaining_capacity = self.capacity - sum(item[1] for item in state)
        max_value = sum(item[0] for item in sorted(state, key=lambda x: x[0]/x[1], reverse=True))
        return max_value if remaining_capacity >= 0 else 0

# List of items (value, weight) and knapsack capacity
items = [(60, 10), (100, 20), (120, 30)]
knapsack_capacity = 50

problem = KnapsackProblem(items, knapsack_capacity)
result = astar(problem)

print("Items selected for the knapsack:")
for action, state in result.path():
    print("Action:", action)
    print("State:", state)
