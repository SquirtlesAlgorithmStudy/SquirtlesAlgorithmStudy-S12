import sys
fastin = sys.stdin.readline 

n = int(fastin())
m = int(fastin())


inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
  graph[a][a] = 0

for _ in range(m):
 a, b, c = map(int,fastin().split())
 graph[a][b] = min(c, graph[a][b])


for k in range(1,n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
  
for a in range(1, n+1):
  for b in range(1, n+1):
    if  graph[a][b] == inf: print(0, end=" ")
    else : print(graph[a][b], end = " ")
  print()