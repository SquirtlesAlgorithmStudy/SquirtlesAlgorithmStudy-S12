import sys
from collections import deque
input = sys.stdin.readline
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(i, j):
    q.append((i, j))
    visited[i][j] = 1
    
    while q:
        x, y = q.popleft()
        
        if x == x2 and y == y2:
            return visited[x][y]-1
            
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    l = int(input())   # 체스판 한 변의 길이
    visited = [[0]*l for _ in range(l)]
    x, y = map(int, input().split())     # 출발 위치
    x2, y2 = map(int, input().split())     # 도착 위치

    q = deque()
    print(bfs(x, y))