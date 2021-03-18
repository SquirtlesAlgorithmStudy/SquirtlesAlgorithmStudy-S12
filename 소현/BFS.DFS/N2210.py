# 작성자 : SH_WON_96
# 2021-03-19
# 알고리즘 - DFS/BFS
# 문제번호 : 2210 숫자판 점프

import sys
#sys.setrecursionlimit(10**7)
fast_in = sys.stdin.readline

matrix = [list(fast_in().strip().split()) for _ in range(5)]

numcase = set([])

def dfs(x,y,text,numc):  #
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if len(text) == 6:
                numc.add(text)
                return numc
            dfs(nx,ny,text + matrix[nx][ny],numc)


visited = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        dfs(i,j,matrix[i][j],numcase)

print(len(numcase))

#print(numcase)