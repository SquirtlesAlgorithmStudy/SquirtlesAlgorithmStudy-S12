# 작성자 : SH_WON_96
# 2021-03-12
# 알고리즘 - BFS
# 문제번호 : 3055 탈출

import sys
from collections import deque
fast_in = sys.stdin.readline

R,C = map(int, fast_in().strip().split())
visited = [[0]*C for _ in range(R)]
matrix = []
qS = deque([]) # 고슴도치의 deque
qW = deque([]) # 물의 deque

for i in range(R):
    line = list(fast_in().strip())
    matrix.append(line)
    for j in range(C):
        if line[j] == "S":
            qS.append((i,j))
            matrix[i][j] = 0
            visited[i][j] = 1
        if line[j] == "*":
            qW.append((i,j))
        if line[j] == "D":
            target = [i,j]

dx = [1,-1,0,0] # 상하좌우
dy = [0,0,-1,1]

while qS or qW:
    # 초단위로 움직이려고 tmp로 만들어서 while 돌림
    tmp1 = []
    tmp2 = []
    while qS:
        sx, sy = qS.popleft()
        if matrix[sx][sy] != "*": # 물이 차지했을수도 있으니깐
            for i in range(4):
                nsx = sx + dx[i]
                nsy = sy + dy[i]
                # 범위안에 있으며 아직 방문 안했고, X도, *도 아닌 값
                if 0 <= nsx < R and 0 <= nsy < C and visited[nsx][nsy]==0 and matrix[nsx][nsy]!="X" and matrix[nsx][nsy] != "*":
                    matrix[nsx][nsy] = matrix[sx][sy] + 1 # D도 값을 업데이트하게 됨
                    visited[nsx][nsy] = 1 # 방문처리
                    tmp1.append((nsx,nsy))

    while qW:
        wx, wy = qW.popleft()
        for i in range(4):
            nwx = wx + dx[i]
            nwy = wy + dy[i]
            if nwx == target[0] and nwy == target[1]: # "D"는 건들면 안되니깐 pass
                continue
            if 0 <= nwx < R and 0 <= nwy < C and matrix[nwx][nwy]!="*" and matrix[nwx][nwy]!="X": 
                matrix[nwx][nwy] = "*"
                tmp2.append((nwx,nwy))

    # 같은 초에서의 움직임 처리 끝났으니까 다음 queue 시작하도록 tmp 값 넣어주기.
    for t in tmp1:
        qS.append(t)
    for t in tmp2:
        qW.append(t)



result = matrix[target[0]][target[1]]

print(result if result!="D" else "KAKTUS")
