from collections import deque
import sys
input = sys.stdin.readline

def bfs(G, V, start):
  queue = deque()
  V[start] = 1
  queue.append(start)
  while queue:
    num = queue.popleft()
    for i in range(1,n+1):
      if V[i] == 0 and G[num][i] == 1:
        queue.append(i)
        V[i] = V[num]+1
  return V

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0
print(graph)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

visited = (bfs(graph, visited, 1))

for i in range(2,n+1):
  if visited[i]<=3 and visited[i]>0: cnt+=1

print(cnt)