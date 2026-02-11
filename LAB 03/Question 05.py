print("Learning Agent Game\n")

qtable = {"Play":0, "Rest":0}

for t in range(1,11):
 if qtable["Play"] <= qtable["Rest"]: action, rew = "Play", 5
 else: action, rew = "Rest", 1
 qtable[action] += rew
 print(f"Step {t}: Action chosen → {action}, Reward received → {rew}")

print("\nQ-table Updated")
print(qtable)
