from collections import deque
import sys
input = sys.stdin.readline
# 2차원 BFS
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  q = deque()
  q.append([x,y])
  visited[x][y] = 1
  vq, oq = [], []  # 늑대 / 양 좌표 기록용

  while q:
    x, y = q.popleft()
    # 늑대 있는 좌표(x,y) vq에 추가
    if farm[x][y] == 'v': vq.append([x,y]) 
    # 양 있는 좌표(x,y) oq에 추가
    elif farm[x][y] == 'o': oq.append([x,y])
    for i in range(4): #상하좌우
      nx = x+dx[i]
      ny = y+dy[i]
      if (nx>=0 and nx<r) and (ny>=0 and ny<c):
        if farm[nx][ny]!='#' and visited[nx][ny]==0:
          visited[nx][ny] = 1
          q.append([nx,ny])
  # 영역별 양 vs 늑대
  if len(vq)>=len(oq): # 늑대가 더 많으면
    # 양 죽음 (양이 있던 곳은 빈자리)
    for i in oq: farm[i[0]][i[1]] = '.' 
  else: # 양이 더 많으면
    # 늑대를 뚜까팸 (있던 곳은 빈자리)
    for i in vq: farm[i[0]][i[1]] = '.'

r, c = map(int, input().split())
farm = [list(map(str,input().rstrip())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

for i in range(r):
  for j in range(c):
    if farm[i][j]!='#' and visited[i][j]==0:
      bfs(i,j)  # 늑대 vs 양
# 아침이 밝았습니당
# 모든 영역의 늑대랑 양 갯수 세기
o_cnt, v_cnt = 0, 0
for i in range(r):
  for j in range(c):
    if farm[i][j]=='o': o_cnt+=1
    elif farm[i][j]=='v':v_cnt+=1

print(o_cnt,v_cnt)