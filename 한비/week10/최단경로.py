import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

V,E=map(int, input().split())#정점개수 간선개수
 
G=[[] for _ in range(V+1)]#그래프 저장
s=int(input()) #시작점

for _ in range(E):#간선받아서 그래프에 저장
    start,end,distance=map(int, input().split())
    G[start].append([distance,end])
 
result = [INF for _ in range(V+1)]#결과저장
result[s]=0
 
q=[]#우선순위 큐
heapq.heappush(q,[0,s])#거리를 앞에두어 우선순위 큐에 넣을때 거리가 비교되도록한다.
 
while q:
    dis, end=heapq.heappop(q)#큐에서 pop
    for d, x in G[end]:#연결된 노드 탐색
        d+=dis#이전거리와 현재 연결된 노드의 거리를 더해서
        if d<result[x]:#거리비교 #거리가 이전보다 짧으면
            result[x]=d#거리를 갱신시키고
            heapq.heappush(q,[d,x])#우선순위 큐에 넣어준다.
 
for i in range(1,V+1):
    print(result[i] if result[i]!=INF else "INF")