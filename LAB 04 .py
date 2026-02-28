#A building floor is represented as a grid:
#building = [
#[1, 1, 0, 1],
#[0, 1, 1, 1],
#[1, 1, 0, 1],
#[1, 0, 1, 1]
#]
#Where 1 = Walkable path, 0 = Blocked path
#Start position: (0,0)
#Emergency Exit: (3,3)
#Movement allowed: Up, Down, Left, Right
#Requirements:
#1. Convert grid into graph (adjacency list).
#2. Implement Breadth-First Search.
#3. Print traversal order and shortest path.
building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

rows = len(building)
cols = len(building[0])

#movements: Up, Down, Left, Right
directions = [(-1,0), (1,0), (0,-1), (0,1)]

graph = {}

for r in range(rows):
    for c in range(cols):
        if building[r][c] == 1: 
            graph[(r, c)] = []         
            for dr, dc in directions:    
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if building[nr][nc] == 1:
                        graph[(r, c)].append((nr, nc))

# BREADTH FIRST SEARCH

def bfs(graph, start, goal):
    visited = []
    parent = {}
    queue = []
    traversal = []

    queue.append(start)
    visited.append(start)
    parent[start] = None

    while queue:
        current = queue.pop(0) 
        traversal.append(current)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # -------- shortest path using parent --------
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    return traversal, path

# RUN BFS
start = (0, 0)
exit = (3, 3)

traversal_order, shortest_path = bfs(graph, start, exit)

print("Adjacency List:")
for key in graph:
    print(key, ":", graph[key])

print("\nBFS Traversal Order:")
print(traversal_order)

print("\nShortest Path from Start to Exit:")
print(shortest_path)
