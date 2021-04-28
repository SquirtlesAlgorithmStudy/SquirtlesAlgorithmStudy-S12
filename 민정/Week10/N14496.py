import sys
from collections import deque

def bfs(a,b):
  q = deque()
  q.append(a)
  check[a] = 0
  while q:
    node = q.popleft()
    if node == b:
      return check[node]
    for i in graph[node]:
      if check[i] == -1:
        q.append(i)
        check[i] = check[node] + 1

  return -1

a, b = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, sys.stdin.readline().split())
  if x == y : continue
  graph[x].append(y)
  graph[y].append(x)

check = [-1]*(N+1)
print(bfs(a,b))