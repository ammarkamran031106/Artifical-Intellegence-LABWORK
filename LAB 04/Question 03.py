#Start node: 'A'
#Goal node: 'G'
#Requirements:
#1. Implement Iterative Deepening Search.
#2. Show each depth level clearly.
#3. Print final path when goal is found.
graph = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F'],
'D': ['G'],
'E': [],
'F': ['H'],
'G': [],
'H': []
}
def dls(node,goal,depth,path):
  if depth == 0:
    return False
  if node == goal:
    return True
  if node not in graph:
    return False
  for child in graph[node]:
    if(dls(child,goal,depth-1,path)):
      path.append(node)
      return True
  return False

def iddfs(node,goal,max_depth):
  for depth in range(max_depth+1):
    print(f"Depth: {depth}")
    path = []
    if(dls(node,goal,depth,path)):
      print("\nPath to goal:" ," →".join(reversed(path)))
      return



iddfs('A','G',4)
