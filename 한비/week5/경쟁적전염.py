from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())

graph=[]
for i in range(N):
    graph.append(list(map(int, stdin.readline().split())))
    
virus=[] 

#방향
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

S, X, Y =map(int,stdin.readline().split()) #시간, 좌표

#bfs 선언
def bfs():
    while queue:
        v,t,x,y=queue.popleft() #바이러스번호, 시간, 좌표
        if S==t: #시간까지
            break
        for i in range(len(dx)):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<N and 0<=new_y<N and graph[new_x][new_y]==0: #아직 방문안했으면
                graph[new_x][new_y]=v
                queue.append((v,t+1,new_x,new_y)) #바이러스번호, 시간 +1, 좌표

#바이러스 정보 append
for i in range(N):
    for j in range(N):
        if graph[i][j]>0: #바이러스가 있으면
            virus.append((graph[i][j],0,i,j)) #바이러스번호, 0(시간), 좌표

virus.sort() #낮은번호부터 증식
# print(virus)

queue=deque(virus)
bfs()

print(graph[X-1][Y-1])