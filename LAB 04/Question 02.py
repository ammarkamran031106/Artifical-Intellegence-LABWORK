#Implement Depth-Limited Search using recursion.
#2. Add depth limit as parameter.
#3. Show nodes visited and path if goal found.
#4. Run with depth = 2 and depth = 3.

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
def dls(graph, start, goal, depth_limit):
  visited = []
  def dfs(node, depth):
      if depth > depth_limit:
        return None #
      visited.append(node)
      if node == goal:
          print(f"Goal found with DLS. Path: {visited}")
          return visited
      for neighbor in graph.get(node, []):
          if neighbor not in visited:
              path = dfs(neighbor, depth + 1)
              if path:
                  return path
      visited.pop() 
      return None
  return dfs(start, 0)


dls(graph,'A','H', 4)
