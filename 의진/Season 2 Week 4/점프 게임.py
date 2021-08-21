import sys
from collections import deque
fastin = sys.stdin.readline
n, k = map(int, fastin().strip().split())
left_data = list(map(int, fastin().strip()))
right_data = list(map(int, fastin().strip()))
visited = [[0] * 2 for _ in range(n)]

def action_1(x, y):
  return (x+1, y)

def action_2(x, y):
  return (x-1, y)

def action_3(x, y):
  return (x+k, 1-y)

action_list = [action_1, action_2, action_3]

def bfs(left_data, right_data, n, k):
  q = deque()
  q.append((0,0,0))
  visited[0][0] = 1

  while q:
    x, y, depth = q.popleft()
  
    for i in range(3):
      nx, ny = action_list[i](x,y)
      if nx >= n:
        return 1
      if depth + 1 <= nx and visited[nx][ny] == 0:
        if (ny == 0 and left_data[nx] == 1) or (ny == 1 and right_data[nx]== 1):
          visited[nx][ny] = 1
          q.append((nx, ny, depth + 1))


  return 0

print(bfs(left_data, right_data, n, k))