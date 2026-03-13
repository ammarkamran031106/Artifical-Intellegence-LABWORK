# operations
def generate(x):
    return [x+2, x+3, x*2]

goal = 20

# heuristic function
def h(n):
    return abs(goal - n)

# Beam Search function
def beam_search(start, goal, beam_width=2):

    beam = [(h(start), [start])]   # (heuristic, path)

    while beam:
        candidates = []

        for cost, path in beam:
            current = path[-1]

            if current == goal:
                return path

            # generate next states
            for nxt in generate(current):
                new_path = path + [nxt]
                candidates.append((h(nxt), new_path))

        # keep best k states
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:beam_width]

        print("Current Beam:", beam)

    return None


# Run Beam Search
start = 1
beam_width = 2

result = beam_search(start, goal, beam_width)

print("\nFinal Path:", result)
