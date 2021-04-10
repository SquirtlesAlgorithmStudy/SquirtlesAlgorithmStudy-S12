import sys
from collections import deque

input=sys.stdin.readline

n = int(input())
a = [list(input().strip()) for _ in range(n)] #입력으로 주어지는
dist = [[-1]*n for _ in range(n)] #방 바꾼 횟수

dx=[-1,0,1,0] 
dy=[0,1,0,-1]

def bfs():
    q = deque()
    q.append((0, 0)) #시작노드 큐에 삽입
    dist[0][0] = 0 #방문처리 및 횟수계산시작
    while q:
        x, y = q.pop() #큐 뒤에서 값 가져오기 / popleft()로하면 흰방 검은방 바꿔줘야함
        if x == n-1 and y == n-1: #마지막노드 도착하면 반환
            print(dist[x][y])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] == -1: 
                if a[nx][ny] == 1: #흰방이라면
                    dist[nx][ny] = dist[x][y] #거리 업데이트 x (0으로)
                    q.append((nx, ny)) #큐뒤에넣기
                else: #검은방이라면
                    dist[nx][ny] = dist[x][y]+1 #횟수 업데이트
                    q.appendleft((nx, ny)) #큐앞에넣기 -> 흰 방 먼저 방문하도록

bfs()

