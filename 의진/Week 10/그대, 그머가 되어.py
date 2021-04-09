import sys
import heapq
inf = int(1e9)
fastin = sys.stdin.readline

a, b = map(int, fastin().split())
n, m = map(int, fastin().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  p, q = map(int,fastin().split())
  graph[p].append(q)
  graph[q].append(p)

distance = [inf] * (n+1)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue 
    for i in graph[now]:
      cost = dist + 1
      if cost < distance[i]:
        distance[i] = cost
        heapq.heappush(q,(cost, i))
dijkstra(a)
if distance[b] == inf: print(-1) 
else: print(distance[b])