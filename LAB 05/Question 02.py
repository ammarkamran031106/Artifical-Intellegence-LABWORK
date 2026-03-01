import random

# Graph
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

# Heuristic values
heuristic = {
    'A': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

# A* Search
def astar(start, goal, graph, heuristic):
    open_list = [(heuristic[start], 0, start)]
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        open_list.sort()
        f, current_g, node = open_list.pop(0)

        if node == goal:
            break

        for neighbor, cost in graph[node].items():
            new_g = current_g + cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_cost = new_g + heuristic[neighbor]
                parent[neighbor] = node
                open_list.append((f_cost, new_g, neighbor))

    # Path reconstruction
    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = parent[n]
    path.reverse()

    return path, g_cost[goal]

# Random edge cost update
def update_edge_cost(graph):
    u = random.choice(list(graph.keys()))
    if graph[u]:
        v = random.choice(list(graph[u].keys()))
        old_cost = graph[u][v]
        new_cost = random.randint(1, 15)
        graph[u][v] = new_cost
        print(f"Edge cost changed: {u} → {v} : {old_cost} → {new_cost}")

# ---------------- RUN ----------------
start = 'A'
goal = 'G'

print("Initial A* Path:")
path, cost = astar(start, goal, graph, heuristic)
print(path, "Cost:", cost)

print("\nDynamic edge cost update:")
update_edge_cost(graph)

print("\nRecomputed A* Path after change:")
path, cost = astar(start, goal, graph, heuristic)
print(path, "Cost:", cost)
