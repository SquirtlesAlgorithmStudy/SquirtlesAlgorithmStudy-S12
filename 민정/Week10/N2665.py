# BFS
# deque 사용

from collections import deque

n = int(input())
a = [list(input().strip()) for _ in range[n]]
dist = [[-1]*n for _ in range(n)] 

def BFS() :
  q = deque()
  q.append((0,0))
  dist[0][0] = 0

  while q:
    x, y = q.pop()
    if x == n-1 and y == n-1:
      print(dist[x][y])
      return
    
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
      nx = x+dx
      ny = y+dy
      if (nx<0) or (nx>=n) or (ny<0) or (ny>=n): continue
      if dist[nx][ny] == -1:
        if a[nx][ny] == '1':
          dist[nx][ny] = dist[x][y]
          q.append((nx, ny))
        else :
          dist[nx][ny] = dist[x][y] + 1
          q.appendleft((nx, ny))

BFS()