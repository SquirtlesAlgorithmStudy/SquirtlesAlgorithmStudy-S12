import sys

INF = sys.maxsize
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
#[[float("inf")]*(n+1) for _ in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]]

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a][b] = min(c, graph[a][b]) 

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if a==b: graph[a][b] = 0
      else : graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=" ")
    else:
      print(graph[a][b], end=" ")
  print()