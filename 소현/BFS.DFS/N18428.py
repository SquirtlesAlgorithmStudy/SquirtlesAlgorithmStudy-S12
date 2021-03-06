# 작성자 : SH_WON_96
# 2021-03-03
# 알고리즘 - BFS
# 문제번호 : 18428 감시 피하기

import sys
from collections import deque
import copy
fast_in = sys.stdin.readline

N = int(fast_in().strip())

table = []

for _ in range(N):
    table.append(fast_in().strip().split(" "))

loc = [] # X 좌표들
teach = [] # T 좌표들
for i in range(N):
    for j in range(N):
        if table[i][j] == "X":
            loc.append((i,j))
        if table[i][j] == "T":
            teach.append((i,j))

result = ""

# M[x][y]
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]
def bfs(g,ans): # graph 받아서 해당 그래프에서
    tch = deque(copy.deepcopy(teach))
    while tch:
        tx, ty = tch.popleft()
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                while 0<= nx < N and 0<= ny < N :
                    if g[nx][ny] == "O":
                        break
                    if g[nx][ny]=="S":
                        ans = "NO"
                        break
                    nx += dx[i]
                    ny += dy[i]

        if ans == "NO":
            return ans

    return ""


# X 중에 3개 바꾸기

for i in range(len(loc)):
    for j in range(i+1,len(loc)):
        for k in range(j+1,len(loc)):
            xi, yi = loc[i]
            xj, yj = loc[j]
            xk, yk = loc[k]

            tabletmp = copy.deepcopy(table)
            tabletmp[xi][yi] = "O"
            tabletmp[xj][yj] = "O"
            tabletmp[xk][yk] = "O"
            result = bfs(tabletmp,"")
            if result == "":
                break
        if result == "":
            break

    if result == "":
        break



print("YES") if result== "" else print("NO")


