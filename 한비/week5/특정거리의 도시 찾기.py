from collections import deque
import sys 
input = sys.stdin.readline
N,M,K,X = map(int, input().split()) #도시, 도로, 거리, 출발도시
dis = [-1] * (N + 1)#최단거리 저장
dis[X]=0 #출발도시 거리는 0
 
graph = [[] for _ in range(N + 1)]
#각 노드가 연결된 정보를 리스트에 저장
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
#BFS수행
q=deque([X]) #시작도시로 설정
while q:
    now = q.popleft()
    for i in graph[now]: #현재 도시에서 이동할 수 있는 모든 도시 확인
        if dis[i] == -1: #방문하지않았다면
            dis[i]==dis[now]+1 #거리 업데이트
            q.append(i) #다시 마지막 방문한 도시 넣어주기
            
for i in range(N+1):
    if dis[i]==K:
        print(i)
if K not in dis:
    print(i)
