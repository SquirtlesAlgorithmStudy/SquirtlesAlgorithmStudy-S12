import sys
from collections import deque


def bfs():
    q = deque()
    q.append((0,0))
    #cnt = 0 #점프횟수
    visited[0]=True
    while q:
        x, y = q.popleft() #x:위치(인덱스) /y:점프횟수
        if x + 1 == n:
            return y

        for i in range(m[x]+1): #점프해서 갈 수 있는 곳 
            jump = x + i
            #jump한곳이 n보다 작고 값이 0보다 크고(0이면 점프못함) 방문안한곳이라면
            if jump<n and m[jump]>0 and not visited[jump]:
                visited[jump] = True #방문처리
                q.append((jump, y+1))
                #cnt=cnt+1
    return -1

input=sys.stdin.readline
n = int(input())
m = list(map(int, input().split()))

visited = [False] * n
print(bfs())