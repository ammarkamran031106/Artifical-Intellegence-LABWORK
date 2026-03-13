import random

# function f(x)
def f(x):
    return -x*x + 6*x


# generate neighbors (x-1 and x+1)
def get_neighbors(x):
    neighbors = []

    if x - 1 >= 0:
        neighbors.append(x - 1)

    if x + 1 <= 6:
        neighbors.append(x + 1)

    return neighbors


# simple hill climbing
def simple_hill_climbing():

    # random start
    x = random.randint(0,6)

    print("Initial x:", x)
    print("f(x):", f(x))

    while True:

        neighbors = get_neighbors(x)

        best = x

        for n in neighbors:
            if f(n) > f(best):
                best = n

        # stop if no better neighbor
        if best == x:
            break

        x = best
        print("Move to x:", x, " f(x):", f(x))

    return x


# run hill climbing
result = simple_hill_climbing()

print("\nFinal optimal x:", result)
print("Maximum value:", f(result))
