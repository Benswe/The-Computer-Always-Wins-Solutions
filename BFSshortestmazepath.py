maze = [
    ["S", 0,   0,   "X", 0],
    ["X", "X", 0,   "X", 0],
    [0,   0,   0,   0,   0],
    [0,   "X", "X", "X", 0],
    [0,   0,   0,   "E", 0]]

def is_valid_square(maze, row, col):
    if maze[row][col] == "X":
        return False
    return True

def is_valid_connection(maze, prev_row, prev_col, row, col):
    # its 100p not a valid connection if the square is an x
    if not is_valid_square(maze, row, col):
        return False
    # to be a valid connection, the last connection in the path must be able to reach row, col in one move(RIGHT, LEFT, UP, DOWN)
    # since we can't move diagonally, either prev_row = row or prev_col = col
    if prev_row == row:
        if (prev_col + 1) == col or (prev_col - 1) == col:
            return True
    if prev_col == col:
        if (prev_row + 1) == row or (prev_row - 1) == row:
            return True
    return False





    

def shortest_maze_path(maze):
    paths = [[(0,0)]]
    used_paths = [(0,0)]
    while len(paths) >= 0:
        path_to_expand = paths.pop(0) # capture and remove the next path we want to search
        last_connection = path_to_expand[-1]
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                if is_valid_connection(maze, last_connection[0], last_connection[1], row, col):
                    if (row, col) not in used_paths:
                        new_path = path_to_expand.copy() # creating our new path
                        new_path.append((row, col))
                        paths.append(new_path)
                        used_paths.append((row,col)) # we don't want to search over this path again after adding it, that would be redundant

                        if maze[row][col] == "E":
                            print(f"Shortest path found length is: {len(new_path)}")
                            print(new_path)
                            return
    print("No path found") # for debugging (should only happen if maze is weird)                        
                        
                    
shortest_maze_path(maze)