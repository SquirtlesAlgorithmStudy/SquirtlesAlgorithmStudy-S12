# 작성자 : SH_WON_96
# 2021-04-28
# 알고리즘 - BFS
# 문제번호 : 3184 양

# 초기 입력값 받기
import sys
from collections import deque
fast_in = sys.stdin.readline

R, C = map(int, fast_in().strip().split())

# . 빈필드 / # 울타리 / o 양 / v 늑대

dx = [-1,1,0,0]
dy = [0,0,-1,1]

matrix = []
visited = [[0]*C for _ in range(R)]
where = []
for i in range(R):
    tmp = list(fast_in().strip())
    matrix.append(tmp)
    for j in range(C):
        if tmp[j] == "v" or tmp[j] == "o":
            where.append((i,j))

def dfs(x,y):
    vnum = 0
    onum = 0
    if matrix[x][y] == "o":
        onum +=1
    if matrix[x][y] == "v":
        vnum += 1
    queue = deque([])
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny <C and matrix[nx][ny]!= "#" and visited[nx][ny]== 0:
                visited[nx][ny] = 1
                if matrix[nx][ny] == "o":
                    onum += 1
                elif matrix[nx][ny] == "v":
                    vnum += 1

                queue.append((nx,ny))

    if onum > vnum:
        vnum = 0
    else:
        onum = 0

    return onum, vnum

vtotal = 0
ototal = 0
# for i in range(R):
#     for j in range(C):
for (i,j) in where:
    if visited[i][j] == 0:
        if matrix[i][j] == "o" or matrix[i][j] == "v" :
            visited[i][j] = 1
            v1,o1 = dfs(i,j)
            vtotal += v1
            ototal += o1

print(str(vtotal)+ " "+ str(ototal))