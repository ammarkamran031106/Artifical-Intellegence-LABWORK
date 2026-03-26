tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

visited = []

def minimax(node, depth, is_max):

    if depth == 0 or isinstance(node, int):
        visited.append(node)
        return node

    if is_max:
        best = -1000
        for child in node:
            value = minimax(child, depth - 1, False)
            if value > best:
                best = value
        return best
    else:
        best = 1000
        for child in node:
            value = minimax(child, depth - 1, True)
            if value < best:
                best = value
        return best

result = minimax(tree, 3, True)

print("part 1:")
print("root value =", result)

print("\npart 2:")
print("visited nodes =", visited)

def minimax_limit(node, depth, is_max):
    if depth == 0:
        if isinstance(node, list):
            if isinstance(node[0], list):
                return node[0][0]
            else:
                return node[0]
        return node

    if isinstance(node, int):
        return node

    if is_max:
        best = -1000
        for child in node:
            value = minimax_limit(child, depth - 1, False)
            if value > best:
                best = value
        return best
    else:
        best = 1000
        for child in node:
            value = minimax_limit(child, depth - 1, True)
            if value < best:
                best = value
        return best

depth_result = minimax_limit(tree, 2, True)
print("\npart 3:")
print("depth limited value =", depth_result)
