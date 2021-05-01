import sys
fastin = sys.stdin.readline

n = int(fastin())
m = int(fastin())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int,fastin().split())
  graph[a].append(b)
  graph[b].append(a)
result = set(graph[1])

for i in graph[1]:
  result.update(graph[i])
print(len(result)-1)