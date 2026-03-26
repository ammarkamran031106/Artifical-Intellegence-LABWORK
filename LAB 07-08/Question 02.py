tree = [
    [[4, 7], [2, 5]],
    [[1, 8], [3, 6]]
]

visited_ab = []
visited_mm = []
values_ab = {}
pruned = []


def minimax(node, depth, is_max):
    if depth == 0 or isinstance(node, int):
        visited_mm.append(node)
        return node

    if is_max:
        best = -1000
        for child in node:
            best = max(best, minimax(child, depth - 1, False))
        return best
    else:
        best = 1000
        for child in node:
            best = min(best, minimax(child, depth - 1, True))
        return best


def alphabeta(node, depth, alpha, beta, is_max, name):

    if depth == 0 or isinstance(node, int):
        visited_ab.append(node)
        return node

    if is_max:
        best = -1000
        for i, child in enumerate(node):
            val = alphabeta(child, depth - 1, alpha, beta, False, name + str(i))
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                pruned.append(name + " branch pruned")
                break

        values_ab[name] = best
        return best

    else:
        best = 1000
        for i, child in enumerate(node):
            val = alphabeta(child, depth - 1, alpha, beta, True, name + str(i))
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                pruned.append(name + " branch pruned")
                break

        values_ab[name] = best
        return best


mm_result = minimax(tree, 3, True)
ab_result = alphabeta(tree, 3, -1000, 1000, True, "Root")

print("minimax root =", mm_result)
print("alpha-beta root =", ab_result)

print("\nminimax visited =", len(visited_mm))
print("alpha-beta visited =", len(visited_ab))

print("\nnode values =", values_ab)
print("\npruned nodes =", pruned)
