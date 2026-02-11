print("Firefighting Robot Simulation\n")

env = {'a':'safe','b':'safe','c':'fire','d':'safe','e':'fire','f':'safe','g':'safe','h':'safe','j':'fire'}
route = ['a','b','c','d','e','f','g','h','j']

def showEnv():
 rooms = ['a','b','c','d','e','f','g','h','j']
 for i in range(0,9,3):
  rrow = rooms[i:i+3]
  for rm in rrow:
   print("F" if env[rm]=="fire" else ".", end=" ")
  print()

print("Initial Environment State:")
showEnv()

for rm in route:
 print("Robot moved to room", rm)
 if env[rm]=="fire": print("Fire detected! Extinguishing fire..."); env[rm]="safe"
 else: print("Room is already safe")
 showEnv()

print("Final Environment: All rooms are safe")
showEnv()
