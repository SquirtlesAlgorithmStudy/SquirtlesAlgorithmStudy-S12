# 작성자 : SH_WON_96
# 2021-03-02
# 알고리즘 - BFS
# 문제번호 : 18405 경쟁적 전염


import sys
from collections import deque
fast_in = sys.stdin.readline

N, K = map(int,fast_in().strip().split(" "))

table =[]
where = deque([])

# table 형성
for i in range(N):
    tmp = list(map(int, fast_in().strip().split(" ")))
    # 바이러스가 존재하는 칸을 미리 deque에 받아 놓음
    for j in range(len(tmp)):
        if tmp[j] != 0:
            where.append((i,j,tmp[j],0))
    table.append(tmp)

S,X,Y = map(int,fast_in().strip().split(" "))

# table[x][y] 일 때
dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

"""
처음에 작은놈부터 시작하면 그다음 queue들은 자동으로 작은애들부터 주변을 탐색하게 되어있음 ㅠㅠ
"""
where = deque(sorted(where, key=lambda x:x[2]))

while where:
    x,y,vtype,sec = where.popleft()

    if sec == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0: # 감염되지 않았다면
            table[nx][ny] = vtype # 감염되지 않았다면 x,y로부터 넘어왔으니 그걸로 감염되어야하지!
            where.append((nx,ny,vtype,sec+1))


print(table[X-1][Y-1])

"""
import sys
from collections import deque

fast_in = sys.stdin.readline

N, K = map(int, fast_in().strip().split(" "))

table = []
time = [[-1] * N for _ in range(N)]
where = deque([])

# table 형성
for i in range(N):
    tmp = list(map(int, fast_in().strip().split(" ")))
    # 바이러스가 존재하는 칸을 미리 deque에 받아 놓음
    for j in range(len(tmp)):
        if tmp[j] != 0:
            where.append((i, j))
            time[i][j] = 0
    table.append(tmp)

S, X, Y = map(int, fast_in().strip().split(" "))

# table[x][y] 일 때
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]
sec = 0
while where:
    x, y = where.popleft()
    if time[x][y] == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == 0:  # 바이러스 옆칸이 감염되지 않았다면
            changed = False
            for j in range(4):  # 해당 칸 주변에 더 낮은 숫자의 바이러스가 있는지 확인해야함.
                nnx = nx + dx[j]
                nny = ny + dy[j]
                if 0 <= nnx < N and 0 <= nny < N and table[nnx][nny] != 0 and table[nnx][nny] < table[x][y]: # 0이 아닌 더 낮은 숫자가 nx,ny 주변에 있다면 해당 숫자가 감염됨
                    if (time[nnx][nny] <= time[x][y]): # nnx,nny가 같은 sec에서 바
                        table[nx][ny] = table[nnx][nny]
                        time[nx][ny] = time[nnx][nny] + 1
                        # where.remove(where.index((nnx,nny,sec)))
                        where.append((nx, ny))
                        changed = True

            if not changed:
                table[nx][ny] = table[x][y]  # 감염되지 않았다면 x,y로부터 넘어왔으니 그걸로 감염되어야하지!
                time[nx][ny] = time[x][y] + 1
                where.append((nx, ny))

# for tmp in table:
#     print(tmp)
print(table[X - 1][Y - 1])

"""
"""
4 3
1 0 2 1
0 0 0 0
3 0 0 0
0 0 3 1
1 3 2
"""
