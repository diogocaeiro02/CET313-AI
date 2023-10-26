import heapq
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost
        self.adjacent = {}
        self.parent = None
        self.g_cost = float("inf")

    def add_neighbor(self, neighbor, cost):
        self.adjacent[neighbor] = cost

    def __lt__(self, other):
        return self.g_cost + self.heuristic_cost < other.g_cost + other.heuristic_cost


def astar_search(start, goal):
    open_list = []
    closed_set = set()

    start.g_cost = 0
    heapq.heappush(open_list, start)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for neighbor, cost in current_node.adjacent.items():
            tentative_g_cost = current_node.g_cost + cost

            if neighbor in closed_set and tentative_g_cost >= neighbor.g_cost:
                continue

            if tentative_g_cost < neighbor.g_cost or neighbor not in open_list:
                neighbor.g_cost = tentative_g_cost
                neighbor.parent = current_node
                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)
    return None


A = Node("A", 5)
B = Node("B", 4)
C = Node("C", 3)
D = Node("D", 2)
E = Node("E", 1)
F = Node("F", 0)

A.add_neighbor(B, 12)
A.add_neighbor(F, 16)
A.add_neighbor(C, 16)
B.add_neighbor(A, 12)
B.add_neighbor(C, 12)
C.add_neighbor(B, 12)
C.add_neighbor(A, 16)
C.add_neighbor(D, 10)
D.add_neighbor(C, 10)
D.add_neighbor(E, 14)
E.add_neighbor(D, 14)
E.add_neighbor(F, 15)
F.add_neighbor(E, 15)
F.add_neighbor(A, 16)

G = nx.Graph()
edges = [(A.name, B.name, {'weight': 12}), (A.name, F.name, {'weight': 16}), (A.name, C.name, {'weight': 16}),
         (B.name, A.name, {'weight': 12}), (B.name, C.name,
                                            {'weight': 12}), (C.name, B.name, {'weight': 12}),
         (C.name, A.name, {'weight': 16}), (C.name, D.name,
                                            {'weight': 10}), (D.name, C.name, {'weight': 10}),
         (D.name, E.name, {'weight': 14}), (E.name, D.name,
                                            {'weight': 14}), (E.name, F.name, {'weight': 15}),
         (F.name, E.name, {'weight': 15}), (F.name, A.name, {'weight': 16})]
G.add_edges_from(edges)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=3000,
                 node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title('Nodes Graph')
plt.show()

# Running the A* search algorithm
path = astar_search(C, F)
print("A* path:", path)

# Visualization
plt.title('Graph with A* path')
nx.draw_networkx(G, pos, with_labels=True, node_size=3000,
                 node_color='skyblue')
nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i + 1]) for i in
                                         range(len(path) - 1)], edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
