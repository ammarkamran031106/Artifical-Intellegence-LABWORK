tree = [
    [[4, 7], [2, 5]],
    [[1, 0], [3, 6]]
]

visited_ab = []
pruned = []
values = {}

def minimax(node, depth, is_max, path):

    if depth == 0 or isinstance(node, int):
        return node, path

    if is_max:
        best = -1000
        best_path = []
        for i, child in enumerate(node):
            val, p = minimax(child, depth - 1, False, path + [i])
            if val > best:
                best = val
                best_path = p
        values[str(path)] = best
        return best, best_path

    else:
        best = 1000
        best_path = []
        for i, child in enumerate(node):
            val, p = minimax(child, depth - 1, True, path + [i])
            if val < best:
                best = val
                best_path = p
        values[str(path)] = best
        return best, best_path


def alphabeta(node, depth, alpha, beta, is_max):

    if depth == 0 or isinstance(node, int):
        visited_ab.append(node)
        return node

    if is_max:
        best = -1000
        for child in node:
            val = alphabeta(child, depth - 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                pruned.append("pruned")
                break
        return best

    else:
        best = 1000
        for child in node:
            val = alphabeta(child, depth - 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                pruned.append("pruned")
                break
        return best


result, path = minimax(tree, 3, True, [])
ab_result = alphabeta(tree, 3, -1000, 1000, True)

print("updated minimax value =", result)
print("optimal path =", path)
print("pruned nodes =", pruned)
