print("Restaurant Selector\n")

rests = {"A":{"distance":3,"rating":7},"B":{"distance":5,"rating":9}}
scores = {}

for r in rests:
 score = rests[r]["rating"] - rests[r]["distance"]
 scores[r] = score
 print("Restaurant", r, "Utility =", score)

best = max(scores, key=scores.get)
print("\nSelected Restaurant:", best)
