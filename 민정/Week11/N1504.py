import sys
import heapq
sys.setrecursionlimit(10 ** 9)

INF = sys.maxsize
N, E = map(int, sys.stdin.readline().split()) # 정점, 간선(가중치)
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
heap = [] # 최소 힙을 위한 큐

for _ in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  if c>1000 and c<1 : continue
  else :
    graph[a].append((b,c))
    graph[b].append((a,c))
    
V1, V2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
  heapq.heappush(heap, (0, start))
  dist[start] = 0
  while heap:
    d, now = heapq.heappop(heap)
    if dist[now] < d : continue
    for i in graph[now]:
      cost = d + i[1]
      if cost<dist[i[0]]:
        dist[i[0]] = cost
        heapq.heappush(heap, (cost, i[0]))
  
  return dist


R_1 = dijkstra(1)
R_V1 = dijkstra(V1)
R_V2 = dijkstra(V2)

y = min(R_1[V1] + R_V1[V2] + R_V2[N], R_1[V2] + R_V2[V1] + R_V1[N])
print(y if y<INF else -1)