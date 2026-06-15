import time

class mazeEnv:
    def __init__(self, gamma=0.9, maze = [["S", 0,   0,   "X", 0],
                                        ["X", "X", 0,   "X", 0],
                                        [0,   0,   0,   0,   0],
                                        [0,   "X", "X", "X", 0],
                                        [0,   0,   0,   "E", 0]]):
        self.actions = ["RIGHT", "LEFT", "UP", "DOWN"]
        self.maze = maze
        self.col = 0
        self.row = 0
        self.n_rows = len(maze)
        self.n_cols = len(maze[0])
        self.states = list(range(self.n_rows * self.n_cols))
        self.gamma = gamma
    
    

    def row_col_to_state(self, row, col):
        return row * self.n_cols + col
    
    def state_to_row_col(self, state):
        row = state // self.n_cols
        col = state % self.n_cols
        return row, col
    def is_valid_square(self, row, col):
        if row < 0 or row >= self.n_rows:
            return False
        if col < 0 or col >= self.n_cols:
            return False
        if self.maze[row][col] == "X":
            return False

        return True
    def is_terminal(self, state):
        row, col = self.state_to_row_col(state)
        return (self.maze[row][col] == "E" or self.maze[row][col] == "X") # returns true if state is terminal

    def move(self, state, action): # takes in row column and action and simulates an update of row and col accordingly
        row, col = self.state_to_row_col(state)
        if action == "RIGHT":
            col += 1
        if action == "LEFT":
            col -= 1
        if action == "UP":
            row -= 1
        if action == "DOWN":
            row += 1
        if self.is_valid_square(row, col):
            return self.row_col_to_state(row, col)
        else:
            return state
    
    def reward(self, state, action): # returns reward of 1 if state moving into is the Exit
        reward = 0
        next_state = self.move(state, action)
        next_row, next_col = self.state_to_row_col(next_state) 
        if self.maze[next_row][next_col] == "E":
            reward += 1
        return reward

        
    

    # value iteration to solve

def value_iteration(env, theta=1e-5):
    V = {s: 0.0 for s in env.states}
    policy = {}
    while True:
        delta = 0.0  # to check for convergence
        for s in env.states:
            if env.is_terminal(s):
                continue
            old_V = V[s]
            best_action = None
            best_value = float('-inf')
            for a in env.actions:
                reward = env.reward(s, a)
                next_state = env.move(s, a)
                value = reward + env.gamma * V[next_state]
                if value > best_value:
                    best_value = value
                    best_action = a
            policy[s] = best_action  # update policy with the best action we found
            V[s] = best_value  # calculate our value from that state
            delta = max(delta, abs(V[s] - old_V))  # check for convergence per state
        if delta < theta:
            break
    return policy, V

def render_policy(env, pi):
    for r in range(env.n_rows):
        row_symbols = []
        for c in range(env.n_cols):
            state = env.row_col_to_state(r, c)
            cell = env.maze[r][c]
            if cell == "X":
                row_symbols.append("X")
            elif cell == "E":
                row_symbols.append("E")
            elif cell == "S":
                row_symbols.append("S")
            else:
                action = pi.get(state, None)
                if action == "RIGHT":
                    row_symbols.append("→")
                elif action == "LEFT":
                    row_symbols.append("←")
                elif action == "UP":
                    row_symbols.append("↑")
                elif action == "DOWN":
                    row_symbols.append("↓")
                else:
                    row_symbols.append(".")
        print(" ".join(row_symbols))


maze = mazeEnv()

start = time.time()
policy, V = value_iteration(maze)     
print(f"Time: {time.time() - start}")

render_policy(maze, policy)

        