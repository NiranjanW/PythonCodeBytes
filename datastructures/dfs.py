
# def dfs(gph, start):
#     visited = set()
#     stack =[start]

#     while stack:
#         vertex = stack.pop()

#     if vertex  not in visited:
#         visited.add(vertex)
#         print(vertex)

#         stack.extend(gph[vertex]-visited)




# def main():
#     graph = {
#   'A': set(['B', 'C']),
#   'B': set(['A', 'D', 'E']),
#   'C': set(['A', 'F']),
#   'D': set(['B']),
#   'E': set(['B', 'F']),
#   'F': set(['C', 'E'])
# }
#     dfs (graph , 'A')

# if __name__ == '__main__':
#     main()

def dfs(graph, start):
  # Create a set to store visited vertices
  visited = set()

  # Create a stack to store the vertices to visit
  stack = [start]

  # While the stack is not empty
  while stack:
    # Pop the top vertex from the stack
    vertex = stack.pop()

    # If the vertex has not been visited
    if vertex not in visited:
      # Mark the vertex as visited
      visited.add(vertex)
      print(vertex)

      # Add all of the vertex's neighbors to the stack
      stack.extend(graph[vertex] - visited)

# Example graph
graph = {
  'A': set(['B', 'C']),
  'B': set(['A', 'D', 'E']),
  'C': set(['A', 'F']),
  'D': set(['B']),
  'E': set(['B', 'F']),
  'F': set(['C', 'E'])
}

# Start the DFS at vertex 'A'
dfs(graph, 'A')