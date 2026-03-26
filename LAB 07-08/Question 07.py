from ortools.sat.python import cp_model

N = 4
model = cp_model.CpModel()

queens = [model.NewIntVar(0, N - 1, f"queen_row_{i}") for i in range(N)]

model.AddAllDifferent(queens)

for i in range(N):
    for j in range(i + 1, N):
        model.Add(queens[i] - queens[j] != i - j)
        model.Add(queens[j] - queens[i] != i - j)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
    print("4-Queens Solution:\n")
    for row in range(N):
        line = ""
        for col in range(N):
            if solver.Value(queens[row]) == col:
                line += " Q "
            else:
                line += " _ "
        print(line)

    print("\nQueen positions:")
    for row in range(N):
        print(f"  Row {row} -> Column {solver.Value(queens[row])}")
else:
    print("No Solution Found")
