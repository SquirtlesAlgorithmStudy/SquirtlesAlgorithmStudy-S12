# 작성자 : SH_WON_96
# 2021-03-11
# 알고리즘 - BFS
# 문제번호 : 2468 안전 영역

import sys
from collections import deque
import copy
fast_in = sys.stdin.readline

N = int(fast_in())
matrix = []
for i in range(N):
    matrix.append(list(map(int,fast_in().strip().split(" "))))

dx = [1,-1,0,0] # 상하좌우
dy = [0,0,-1,1]

def dfs(queue,visited,table,section):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and table[nx][ny] == 1:
                    visited[nx][ny] = section
                    queue.append((nx,ny))

maxcount = 0
for h in range(0,101):
    table = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(N):
            if table[i][j] <= h:
                table[i][j] = 0
            else:
                table[i][j] = 1

    visited = [[0]*N for _ in range(N)]
    queue = deque([])
    section = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and visited[i][j] == 0:
                section += 1
                queue.append((i,j))
                visited[i][j] = section
                dfs(queue,visited,table,section)


    maxcount = max(section,maxcount)

print(maxcount)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""