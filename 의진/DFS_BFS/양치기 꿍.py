import sys
from collections import deque
fastin = sys.stdin.readline
r, c = map(int, fastin().strip().split())
board = [list(fastin().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
data =[]
for i in range(r):
    for j in range(c):
      if board[i][j] in 'kv':
        data.append((i, j))
for i, j in data:
  visited[i][j] = 1
        
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(board, visited):
  queue = deque()
  sheep_final = 0
  wolf_final = 0
  for i in range(len(data)):
    if visited[data[i][0]][data[i][1]] == 1:
      nx = data[i][0]
      ny = data[i][1]
      visited[nx][ny] = 2
      queue.append((nx,ny))
      wolf = 0
      sheep = 0
      if board[nx][ny] == 'k' : sheep +=1
      elif board[nx][ny] == 'v' : 
        wolf += 1
      

      while queue:
        x, y = queue.popleft()
        
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if (0 <= nx < r) and (0 <= ny < c) and board[nx][ny] != '#' and visited[nx][ny]!= 2:
            queue.append((nx,ny))
            visited[nx][ny] = 2
            if board[nx][ny] == 'k': sheep += 1
            elif board[nx][ny] == 'v' : wolf += 1


      if wolf >= sheep : wolf_final += wolf
      else : sheep_final += sheep

  return (sheep_final, wolf_final)


sheep_r, wolf_r = bfs(board,visited)
print(sheep_r, wolf_r)