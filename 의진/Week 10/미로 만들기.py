import sys
from collections import deque
fastin = sys.stdin.readline
n = int(fastin())
maze = [[-1] * (n+1)]
maze += [[-1] + list(map(int,list(fastin().strip()))) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
visited = [[-1] * (n+1) for _ in range(n+1)]
queue.append((1, 1))
visited[1][1] = 0
while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 < nx <=n) and (0 < ny <= n):
      if visited[nx][ny] == -1:
        if maze[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          queue.append((nx, ny))
        else:
          visited[nx][ny] = visited[x][y]
          queue.appendleft((nx, ny))
print(visited[n][n])