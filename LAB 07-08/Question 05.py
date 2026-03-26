from ortools.sat.python import cp_model

model = cp_model.CpModel()

A = model.NewIntVar(0, 3, "A")
B = model.NewIntVar(0, 3, "B")
C = model.NewIntVar(0, 3, "C")

model.Add(A != B)
model.Add(B != C)
model.Add(A + B <= 4)

class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables
        self.solution_count = 0

    def on_solution_callback(self):
        self.solution_count += 1
        print(f"Solution {self.solution_count}: ", end="")
        for v in self.variables:
            print(f"{v.Name()} = {self.Value(v)}", end="  ")
        print()

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True

callback = SolutionPrinter([A, B, C])
solver.Solve(model, callback)

print(f"\nTotal solutions found: {callback.solution_count}")
