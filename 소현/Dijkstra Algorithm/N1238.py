# 작성자 : SH_WON_96
# 2021-04-15
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 1238 파티

# 초기 입력값 받기
import sys
import heapq
import copy
fast_in = sys.stdin.readline

N, M, X = map(int, fast_in().strip().split())
connection = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,t = map(int, fast_in().strip().split())
    connection[s].append((e,t))


def dijkstra(a,b):
    weight = [float("INF")]*(N+1)
    heap = []

    weight[a] = 0
    for (v,w) in connection[a]:
        heapq.heappush(heap, (w,v))
        weight[v] = w

    while heap:
        w,v = heapq.heappop(heap)

        if v == b:
            return weight[b]

        for (nv,nw) in connection[v]:
            if w + nw < weight[nv]:
                weight[nv] = w + nw
                heapq.heappush(heap,(w+nw,nv))

    return weight[b]

result = []
for i in range(1,N+1):
    if i == X:
        result.append(0)
        continue
    result.append(dijkstra(i,X)+dijkstra(X,i))

print(max(result))