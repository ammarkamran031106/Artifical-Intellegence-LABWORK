print("Traffic Light Reflex Agent\n")

conds = ["Heavy Traffic", "Light Traffic"]
i = 1

for c in conds:
 print(f"Step {i}")
 if c == "Heavy Traffic":
  print("Percept: Heavy Traffic → Action: Extend Green Time")
 else:
  print("Percept: Light Traffic → Action: Normal Green")
 print("-"*40)
 i += 1

