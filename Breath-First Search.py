import time
from collections import deque


def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    parent = {}  # To keep track of the parent of each cell in the path

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] != '#' and (x, y
                                                                          ) not in visited

    queue = deque([start])
    visited.add(start)
    found = False

    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            found = True
            break
        # Define possible moves: up, down, left, right
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                parent[(new_x, new_y)] = (x, y)

    if not found:
        return "No path found"

    # Reconstruct the path from the goal to the start
    path = []
    x, y = goal
    while (x, y) != start:
        path.append((x, y))
        x, y = parent[(x, y)]

    path.append(start)
    path.reverse()

    # Update the maze with the path
    for x, y in path:
        if maze[x][y] != 'S' and maze[x][y] != 'G':
            maze[x][y] = '*'
    return "Path found"


# Define the corrected maze
maze = [
    ['S', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['#', '#', '#', '.', '#', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', 'G'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# Starting and goal positions
start_time = time.time()
start_position = (0, 0)
goal_position = (2, 8)

result = bfs_maze(maze, start_position, goal_position)
end_time = time.time()

total_time = end_time - start_time

# Print the maze with the path
for row in maze:
    print(' '.join(row))


print(result, 'Time: {:.5f}'.format(total_time))
