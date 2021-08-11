## 유기농 배추
from collections import deque
import sys
fastin = sys.stdin.readline
testcase = int(fastin())

def testcasein(testcase):
  m, n, k = map(int, fastin().strip().split())
  data =[list(map(int,fastin().strip().split())) for _ in range(k)]
  board = [[0] * n for _ in range(m)]
  for i, j in data:
    board[i][j] = 1
  
  return (m, n, k , board, data)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,k,board, data):
  worm = 0
  queue = deque()

  for i in range(k):
    if board[data[i][0]][data[i][1]] == 1:
      nx = data[i][0]
      ny = data[i][1]
      board[data[i][0]][data[i][1]] = 2
      queue.append([nx, ny])

      while queue : 
        x, y = queue.popleft()
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if ( 0 <= nx < m) and (0 <= ny < n):
            if board[nx][ny] == 1:
              queue.append([nx, ny])
              board[nx][ny] = 2

      worm += 1
  return worm

result = []
for _ in range(testcase):
  m,n,k,board,data = testcasein(testcase)
  result.append(bfs(m,n,k,board, data))

for i in range(testcase):
  print(result[i])