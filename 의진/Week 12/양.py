import sys
from collections import deque
fastin = sys.stdin.readline

r, c = map(int,fastin().split())
graph = [list(fastin().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(queue, visited, graph):
  sheep = 0
  wolf = 0
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < r and 0 <= ny < c:
        if visited[nx][ny] == 0 and graph[nx][ny] != '#':
          visited[nx][ny] = 1
          if graph[nx][ny] == 'v':
            wolf += 1
          if graph[nx][ny] == 'o':
            sheep += 1
          queue.append((nx, ny))
  if sheep > wolf : return (1, sheep)
  else : return(0, wolf)

queue = deque()
visited = [[0] * c for _ in range(r)]
s = 0
w = 0
for i in range(r):
  for j in range(c):
    queue.append((i, j))
    a = bfs(queue, visited, graph)
    if a[0] == 0 : w += a[1]
    else : s += a[1]
print(s, w)