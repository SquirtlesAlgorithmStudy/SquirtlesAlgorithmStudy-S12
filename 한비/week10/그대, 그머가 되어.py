from collections import deque
import sys
input = sys.stdin.readline


a, b = map(int, input().split())
n, m = map(int, input().split())
v = [[] for _ in range(n+1)]

dist = [-1]*(n+1)

for i in range(m):
    x, y = map(int, input().split())
    v[x].append(y)
    v[y].append(x)

def bfs():
    q = deque()
    q.append(a)
    dist[a] = 0
    while q:
        x = q.popleft()
        if x == b:
            print(dist[x])
            return
        for nx in v[x]:
            if dist[nx] == -1:
                q.append(nx)
                dist[nx] = dist[x]+1
    print(-1)


bfs()
