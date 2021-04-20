# 작성자 : SH_WON_96
# 2021-04-06
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 2665 미로 만들기

# 초기 입력값 받기
import sys
from collections import deque
fast_in = sys.stdin.readline

N = int(fast_in().strip())

matrix = []
for _ in range(N):
    matrix.append(list(map(int,list(fast_in().strip()))))

#print(matrix)

visited = [[-1]*N for _ in range(N)]

queue  = deque()
queue.append((0,0))
visited[0][0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] == -1:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    # visited 숫자가 올라가서 우선순위가 뒤로 감
                    queue.append((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    # 숫자가 그대로니깐 얘를 먼저 처리해줘야함
                    queue.appendleft((nx, ny))
      


print(visited[N-1][N-1])
