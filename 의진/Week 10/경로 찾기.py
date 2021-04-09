import sys
fastin = sys.stdin.readline

n = int(fastin())
graph= []; graph.append([0]*(n+1))
graph += [[0]+list(map(int,fastin().split())) for _ in range(n)]

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      if graph[a][b] == 0:
        graph[a][b] = graph[a][b] or (graph[a][k] and graph[k][b])
for a in range(1,n+1):
  for b in range(1, n+1):
    print(graph[a][b], end = " ")
  print()