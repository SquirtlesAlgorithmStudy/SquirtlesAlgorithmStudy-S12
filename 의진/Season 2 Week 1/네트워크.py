def generategraph(n, computers):
    graph = [[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1 and i!=j:
                graph[i+1].append(j+1)
    return graph
                
def dfs(node, visited, graph):
  if visited[node] == 0:
    visited[node] = 1
    for i in range(len(graph[node])):
      dfs(graph[node][i], visited, graph)
    return True
  return False


def solution(n, computers):
    answer = 0
    visited = [0] * (n+1)
    graph = generategraph(n, computers)
    for i in range(1, n+1):
      if dfs(i, visited, graph) :
        answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))