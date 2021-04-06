# 작성자 : SH_WON_96
# 2021-04-06
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 1753 최단경로

# 초기 입력값 받기
import sys
import heapq
fast_in = sys.stdin.readline

V,E = map(int, fast_in().strip().split())

start = int(fast_in().strip())

connection = [[] for i in range(V+1)]
weight = [float("INF")]*(V+1)


heap = []
for _ in range(E):
    u,v,w = map(int, fast_in().strip().split())
    connection[u].append([w,v])


weight[start] = 0
heapq.heappush(heap,(0,start))

while heap:
    w,v = heapq.heappop(heap)

    if weight[v] < w:
        continue

    for wei, next_v in connection[v]:
        next_wei = wei + w # 현재 w에서 wei 만큼 추가되는 값
        if next_wei < weight[next_v]: # next_wei가 저장된 값보다 작다면 업데이트
            weight[next_v] = next_wei
            heapq.heappush(heap,(next_wei,next_v))

for _ in weight[1:]:
    if _ != float("inf"):
        print(_)
    else:
        print("INF")



# 그냥하면 시간초과됨. sort떄문에 초과되는 것으로 예상됨
"""
import sys
from collections import deque
fast_in = sys.stdin.readline

V,E = map(int, fast_in().strip().split())

start = int(fast_in().strip())

connection = [[] for i in range(V+1)]
weight = [float("inf")]*(V+1)


for _ in range(E):
    u,v,w = map(int, fast_in().strip().split())
    connection[u].append([w,u,v])

#result = sorted(result,key = lambda s: (-s[1],s[2],-s[3], s[0]))

queue = deque()
weight[start] = 0

#print(connection)
for i in range(V):
    connection[i].sort()
#print(connection)

for s in connection[start]:
    queue.append(s)

while queue:
    w,u,v = queue.popleft()

    if weight[u]+ w < weight[v]:
        weight[v] = weight[u]+w
        for s in connection[v]:
            queue.append(s)

print(weight[1:])
"""