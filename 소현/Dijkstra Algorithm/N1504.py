# 작성자 : SH_WON_96
# 2021-04-06
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 1504 특정한 최단 경로

# 초기 입력값 받기
import sys
import heapq
import copy
fast_in = sys.stdin.readline

N,E = map(int, fast_in().strip().split())
connection = [[] for _ in range(N+1)]

#matrix = [[float("inf")]*(N+1) for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, fast_in().strip().split())
    connection[a].append((b,c))
    connection[b].append((a,c))

v1, v2 = map(int, fast_in().strip().split())



def findlen(x,y):
    tmpweight = [float("inf")]*(N+1)
    heap = []
    visited = [0]*(N+1)
    tmpweight[x] = 0

    for (v, w) in connection[x]:
        heapq.heappush(heap, (tmpweight[x] + w, v))
        tmpweight[v] = tmpweight[x] + w

    while heap:
        w,v = heapq.heappop(heap)
        visited[v] = 1

        # 이거 추가하니까 1312 ms -> 460 ms 로 줄어들었음
        if v == y:
             return tmpweight[y]

        for (nv, nw) in connection[v]:
            if visited[nv] == 0:
                if w + nw < tmpweight[nv]:
                    tmpweight[nv] = w+nw
                    heapq.heappush(heap,(w+nw,nv))


    return tmpweight[y]

t1 = findlen(1,v1)
t2 = findlen(1,v2)
t3 = findlen(v1,v2)
t4 = findlen(v2,N)
t5 = findlen(v1,N)

result = min(t1+t3+t4,t1+t3+t3+t5,t2+t3+t5,t2+t3+t3+t4,t1+t1+t2+t4,t2+t2+t1+t5)
if  result == float("inf"):
    print(-1)
else:
    print(result)
