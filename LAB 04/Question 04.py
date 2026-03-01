#Implement Uniform Cost Search.
#2. Maintain frontier (priority-based), cost tracking, and path reconstruction.
#3. Print least cost path and total cost.
graph = {
'S': {'A': 4, 'B': 2},
'A': {'C': 5, 'D': 10},
'B': {'E': 3},
'C': {'G': 4},
'D': {'G': 1},
'E': {'D': 4},
'G': {}
}
def ucs(start,goal ,graph):
  queue=[(0,start)]
  visited=[]
  parent={}
  cost_so_far={}
  parent[start] = None
  cost_so_far[start] = 0

  while queue:
    queue.sort()
    current_cost,current_node = queue.pop(0)
    if current_node == goal:
      break
    
    if current_node not in visited:
      visited.append(current_node)

    for neighbor , cost in  graph[current_node].items():
      new_cost = current_cost + cost
      
      if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
        cost_so_far[neighbor]=new_cost
        queue.append((new_cost,neighbor))
        parent[neighbor]=current_node


  path = []
  node = goal
  while node is not None:
    path.append(node)
    node=parent[node]
  path.reverse()
  return path,cost_so_far[goal]




print(ucs('S','G',graph))
