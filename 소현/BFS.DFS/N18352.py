# 작성자 : SH_WON_96
# 2021-03-02
# 알고리즘 - BFS
# 문제번호 : 18352 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

N,M,K,X = map(int, input().strip().split(" "))

table = [[] for _ in range(N+1)]

for i in range(M):
    x,y = map(int,input().strip().split(" "))
    table[x].append(y)

queue = deque([])
visited = [-1]*(N+1) # 방문했으면 depth 넣어주기
count = 0
queue.append(X)
visited[X] = 0


while queue:
    x = queue.popleft()
    count += 1

    for ni in table[x]:
        if visited[ni]==-1:
            visited[ni] = visited[x]+1
            queue.append(ni)

isCity = False
for i,v in enumerate(visited):
    if v == K:
        print(i)
        isCity = True

if not isCity:
    print(-1)
