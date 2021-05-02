from collections import deque
import sys
input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append([x,y])
  visited[x][y] = 1
  vq, oq = [], []
  while q:
    x, y = q.popleft()
    if farm[x][y] == 'v': vq.append([x,y])
    elif farm[x][y] == 'o': oq.append([x,y])
    for i in range(4): #상하좌우
      nx = x+dx[i]
      ny = y+dy[i]
      if (nx>=0 and nx<r) and (ny>=0 and ny<c):
        if farm[nx][ny]!='#' and visited[nx][ny]==0:
          visited[nx][ny] = 1
          q.append([nx,ny])
  if len(vq)>=len(oq):
    for i in oq: farm[i[0]][i[1]] = '.'
  else:
    for i in vq: farm[i[0]][i[1]] = '.'

r, c = map(int, input().split())
farm = [list(map(str,input().rstrip())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

for i in range(r):
  for j in range(c):
    if farm[i][j]!='#' and visited[i][j]==0:
      bfs(i,j)

ocnt, vcnt = 0, 0
for i in range(r):
  for j in range(c):
    if farm[i][j]=='o': ocnt+=1
    elif farm[i][j]=='v':vcnt+=1

print(ocnt,vcnt)