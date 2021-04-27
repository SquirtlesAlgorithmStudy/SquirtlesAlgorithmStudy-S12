# 작성자 : SH_WON_96
# 2021-04-27
# 알고리즘 - BFS
# 문제번호 : 2573 빙산

# 초기 입력값 받기
import sys
from collections import deque
import copy
sys.setrecursionlimit(10**5)
fast_in = sys.stdin.readline

N,M = map(int, input().split())
matrix = []
queue = deque([])
for i in range(N):
    tmp = list(map(int,fast_in().strip().split()))
    for j in range(M):
        if tmp[j]>0:
            queue.append((i,j))
    matrix.append(tmp)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def check_section(table):
    visited=[[0]*M for _ in range(N)]
    count = 0
    q = deque([])
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if table[i][j]>0 and visited[i][j]==0:
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    x,y = q.popleft()
                    for t in range(4):
                        nx = x + dx[t]
                        ny = y + dy[t]
                        if 0 <= nx < N and 0 <= ny < M:
                            if visited[nx][ny]== 0 and table[nx][ny] > 0:  # 기존꺼에서 x,y 주변이 0 이면 녹아야하는 갯수 증가
                                visited[nx][ny] = 1
                                q.append((nx,ny))
                count += 1
                if count >= 2:
                    return count
    return count


def bfs(table,q,year):
    ctable = copy.deepcopy(table)
    nextq = deque([])
    while q:
        x,y = q.popleft()
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <N and 0 <= ny < M:
                if table[nx][ny] == 0 : # 기존꺼에서 x,y 주변이 0 이면 녹아야하는 갯수 증가
                    count += 1

        if count > 0: # 녹아야하는게 있으면 ctable에 바꿔주기
            if count >= ctable[x][y]:
                ctable[x][y] = 0
            else:
                ctable[x][y] = ctable[x][y] - count
                nextq.append((x,y))
        elif ctable[x][y] > 0 and count == 0:
            nextq.append((x,y))
    sumtable = 0
    for i in range(N):
        sumtable += sum(ctable[i])
    check = check_section(ctable)
    if check >1:
        print(year+1)
    elif sumtable == 0:
        print(0)
    else:
        bfs(ctable,nextq,year+1)


#print(matrix)
#print(queue)
if check_section(matrix) >=2:
    print(0)
else:
    bfs(matrix,queue,0)