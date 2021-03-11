# 작성자 : SH_WON_96
# 2021-03-11
# 알고리즘 - BFS
# 문제번호 : 1012 유기농 배추

import sys
from collections import deque
fast_in = sys.stdin.readline

T = int(fast_in())

dx = [1,-1,0,0] # 상하좌우
dy = [0,0,-1,1]

def getmatrix():
    M,N,K = map(int,fast_in().strip().split())
    matrix = [[0]*M for _ in range(N)] # N 행 M 열

    for _ in range(K):
        j,i = map(int,fast_in().strip().split())
        matrix[i][j] = 1
    return matrix , M,N,K

def dfs(queue,visited,section,matrix):
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny < M:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visited[nx][ny] = section
                    queue.append((nx,ny))

for i in range(T):
    matrix , M, N, K = getmatrix()
    visited = [[0]*M for _ in range(N)]
    section = 0
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j]==0:
                section += 1
                queue.append((i,j))
                visited[i][j] = section
                dfs(queue,visited,section,matrix)


    print(section)


