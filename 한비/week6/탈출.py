from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph=[]

water=deque() #물

#고슴도치위치, 비버굴 위치 저장
for i in range(r):
    a=list(input())
    for j in range(c):
        if a[j]=='*':
            water.append((i,j)) #물위치저장(물이 여러군데 있을수도있으므로 큐에 저장)
        elif a[j]=='S':
            s=(i,j) #고슴도치위치
        elif a[j]=='D':
            d=(i,j) #비버굴위치
    graph.append((a))

q=deque() #고슴도치
q.append(s) #시작점 큐에 넣기

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

check=False
ans=0 # 횟수

while q:
    if check:
        break
    if water:
        for _ in range(len(water)):
            x,y=water.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.' and graph[nx][ny]!='X':
                    graph[nx][ny]='*' #방문처리
                    water.append((nx,ny))
        for _ in range(len(q)):
            if check:
                break
            x2,y2=q.popleft()
            for i in range(4):
                nx2=x2+dx[i]
                ny2=y2+dy[i]
                
                #고슴도치가 굴에 도착하면
                if d[0]==nx2 and d[1]==ny2:
                    check=True
                    break
                elif 0<=nx2<r and 0<=ny2<c and graph[nx2][ny2]=='.' and graph[nx2][ny2]!='X' and graph[nx2][ny2]!='*':
                    graph[nx2][ny2]=='S' #방문처리
                    graph.append((nx2,ny2))
    ans=ans+1

if check==True:
    print(ans)
else:
    print('KAKTUS')