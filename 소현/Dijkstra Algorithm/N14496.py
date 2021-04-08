# 작성자 : SH_WON_96
# 2021-04-08
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 14496, 그대, 그머가 되어

# 초기 입력값 받기
import sys
from collections import deque
fast_in = sys.stdin.readline

a,b = map(int,fast_in().strip().split())
N,M = map(int,fast_in().strip().split())

matrix = [float("inf")]*(N+1)

connection = [[] for _ in range(N+1)]

for _ in range(M):
    x1,x2 = map(int,fast_in().strip().split())
    connection[x1].append(x2)
    connection[x2].append(x1)

queue = deque()

matrix[a] = 0
for m in connection[a]:
    queue.append((m,1))
    matrix[m] = 1

while queue:
    v,p = queue.popleft()
    for nv in connection[v]:
        if p+1 < matrix[nv]:
            matrix[nv] = p+1
            queue.append((nv,p+1))

if matrix[b] == float("inf"):
    print(-1)
else:
    print(matrix[b])



