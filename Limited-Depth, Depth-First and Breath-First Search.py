from collections import deque
import time

# ----------- Breath-First Search ---------


def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        node, path, = queue.popleft()
        if node == goal:
            return path + [node]
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [node]))
    return None  # Goal not found

# ------------- Depth-First Search -----------


def dfs(graph, node, goal, visited=None):
    if visited is None:
        visited = set()
    if node == goal:
        return [node]
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            path = dfs(graph, neighbor, goal, visited)
            if path:
                return [node] + path
    return None  # Goal not found

# ------------ Limited-Depth Search --------------


def dls(graph, node, goal, depth, visited=None):
    if visited is None:
        visited = set()
    if depth == 0:
        return None
    if node == goal:
        return [node]
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            path = dls(graph, neighbor, goal, depth - 1, visited)
            if path:
                return [node] + path
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'H'],
    'G': ['D', 'H'],
    'H': ['G', 'F']
}

start_node = 'B'
goal_node = 'H'
start_time = time.time()
max_depth = 3


resultbfs = bfs(graph, start_node, goal_node)
resultdfs = dfs(graph, start_node, goal_node)
resultlds = dls(graph, start_node, goal_node, max_depth)

end_time = time.time()


if resultbfs:
    print("Path BFS found:", resultbfs,
          "Time: {:.5f}".format(end_time - start_time), "s")
else:
    print("No path found with Breath-First Search.")

if resultdfs:
    print("Path DFS found:", resultdfs,
          "Time: {:.5f}".format(end_time - start_time), "s")
else:
    print("No path found with Depth-First Search.")

if resultlds:
    print("Path LDS found:", resultlds,
          "Time: {:.5f}".format(end_time - start_time), "s")
else:
    print("No path found with Limited-Depth Search.")
