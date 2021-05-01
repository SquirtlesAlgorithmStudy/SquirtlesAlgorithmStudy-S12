# 변수명 쓸 때 sum, graph 쓰지말기
import sys
from collections import deque
fastin = sys.stdin.readline

n, m = map(int,fastin().split())
graph=[list(map(int,fastin().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(queue, visited, graph):
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
    
      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == 0 and graph[nx][ny] != 0:
          visited[nx][ny] = 1
          queue.append((nx, ny))


def melt(graph):
  new_graph = [[0] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if graph[i][j] != 0:
        count = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 : count += 1
        new_graph[i][j] = max(0, graph[i][j]-count)
  
  return new_graph

t = 0

while True:
  queue = deque()
  graph = melt(graph)
  visited = [[0]*m for _ in range(n)]
  t += 1
  sum = 0
  for i in range(n):
    for j in range(m):
      if graph[i][j] !=0 and visited[i][j] == 0:
        sum += 1
        if sum == 2:
          print(t)
          sys.exit()
        queue.append((i, j))
        bfs(queue, visited, graph)
  if sum == 0 : 
    print(0)
    sys.exit()