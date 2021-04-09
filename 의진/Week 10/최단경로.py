import sys
fastin = sys.stdin.readline

import heapq
inf = int(1e9)

n,m = map(int,fastin().split())
start = int(fastin())
graph = [[] for _ in range(n+1)]
distance = [inf] * (n+1)

for _ in range(m):
  a,b,c = map(int,fastin().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == inf : print("INF")
  else: print(distance[i])