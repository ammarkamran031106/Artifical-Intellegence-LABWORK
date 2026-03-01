# Graph
graph = {
    'S': [('A',3), ('B',6), ('C',5)],
    'A': [('D',9), ('E',8)],
    'B': [('F',12), ('G',14)],
    'C': [('H',7)],
    'H': [('I',5), ('J',6)],
    'I': [('K',1), ('L',10), ('M',2)],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

# UCS (safe)
def ucs(start, goal, graph):
    queue = [(0, start)]
    parent = {start: None}
    cost_so_far = {start: 0}

    while queue:
        queue.sort()
        current_cost, node = queue.pop(0)

        if node == goal:
            break

        for neighbor, cost in graph[node]:
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = node
                queue.append((new_cost, neighbor))

    if goal not in parent:
        return None, float('inf')

    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = parent[n]
    path.reverse()

    return path, cost_so_far[goal]

def multi_goal_best_first(start, goals, graph):
    current = start
    full_path = [start]
    total_cost = 0
    remaining_goals = goals[:]

    while remaining_goals:
        best_goal = None
        best_path = None
        best_cost = float('inf')

        for g in remaining_goals:
            path, cost = ucs(current, g, graph)
            if path is not None and cost < best_cost:
                best_goal = g
                best_path = path
                best_cost = cost

        if best_goal is None:
            print("Some goals are unreachable.")
            break

        full_path.extend(best_path[1:])
        total_cost += best_cost
        current = best_goal
        remaining_goals.remove(best_goal)

    return full_path, total_cost

# RUN
goals = ['D', 'E', 'G', 'K', 'L', 'M']
path, cost = multi_goal_best_first('S', goals, graph)

print("Path covering all reachable goals:")
print(path)
print("Total cost:")
print(cost)
