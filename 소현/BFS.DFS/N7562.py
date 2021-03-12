# 작성자 : SH_WON_96
# 2021-03-12
# 알고리즘 - BFS
# 문제번호 : 7562 나이트의 이동

import sys
from collections import deque
fast_in = sys.stdin.readline

T = int(fast_in())

dx = [-2,-1,1,2,2,1,-1,-2] # 옮겨갈 수 있는 좌표 위치
dy = [1,2,2,1,-1,-2,-2,-1] #


# 최소 몇번만에 도달하는지 구하는거니까 BFS로 풀어야함.

def bfs():
    N = int(fast_in()) # 바둑판 크기
    fx, fy = map(int,fast_in().strip().split()) # from x, from y
    tx, ty = map(int, fast_in().strip().split()) # to x, to y
    matrix = [[0]*N for i in range(N)] # table 먼저 만들기
    queue = deque([])
    queue.append((fx,fy))
    matrix[fx][fy] = 1
    result = 0
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx< N and 0 <= ny < N and matrix[nx][ny] == 0:
                if nx == tx and ny == ty:
                    result =  matrix[x][y]+1
                    return result-1
                else:
                    matrix[nx][ny]=matrix[x][y]+1
                    queue.append((nx,ny))
    return result

for _ in range(T):
    print(bfs())
