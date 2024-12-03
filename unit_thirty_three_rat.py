def is_safe(maze, x, y):
    """Check if maze[x][y] is a valid move."""
    N = len(maze)
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 0

def solve_maze_util(maze, x, y, path):
    """Use backtracking to find the solution to the maze."""
    N = len(maze)
    
    # If (x, y) is the destination, mark it and return True
    if x == N - 1 and y == N - 1:
        path.append((x, y))
        return True
    
    # Check if maze[x][y] is a valid move
    if is_safe(maze, x, y):
        # Mark the current cell as part of the path
        path.append((x, y))
        
        # Move forward in the x direction (right)
        if solve_maze_util(maze, x + 1, y, path):
            return True
        
        # Move down in the y direction
        if solve_maze_util(maze, x, y + 1, path):
            return True
        
        # Move left in the x direction
        if solve_maze_util(maze, x - 1, y, path):
            return True
        
        # Move up in the y direction
        if solve_maze_util(maze, x, y - 1, path):
            return True
        
        # If no direction works, backtrack
        path.pop()
        return False
    
    return False

def print_maze_with_path(maze, path):
    """Print the maze with the solution path marked as 0, and the rest as 1."""
    N = len(maze)
    solution = [[1] * N for _ in range(N)]
    
    for x, y in path:
        solution[x][y] = 0
    
    for row in solution:
        print(" ".join(str(cell) for cell in row))
    print()

def solve_maze(maze):
    """Solve the maze and print the maze with the path if it exists."""
    path = []
    if solve_maze_util(maze, 0, 0, path):
        print("Path found:")
        print_maze_with_path(maze, path)
    else:
        print("No solution exists.")
        print_maze_with_path(maze, path)

# Example usage
maze = [[0, 0, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [0, 0, 0, 0]]

solve_maze(maze)
