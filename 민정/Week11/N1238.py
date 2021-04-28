import sys
import heapq
sys.setrecursionlimit(10 ** 9)

# inp = sys.stdin.readline()
INF = sys.maxsize
N, M, X = map(int, sys.stdin.readline().split()) # 정점, 간선(가중치)
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, Ti = map(int, sys.stdin.readline().split())
  graph[a].append((b,Ti))

def dijkstra(start):
  dist = [INF] * (N+1)
  dist[start] = 0
  heap = [] # 최소 힙을 위한 큐
  heapq.heappush(heap, [dist[start], start])

  while heap:
    d, now = heapq.heappop(heap)
   # if dist[now] < d : continue
    for i, j in graph[now]:
      cost = dist[now] + j
      if cost<dist[i]:
        dist[i] = cost
        heapq.heappush(heap, [cost, i])
  return dist

ans = []
distance_X = dijkstra(X)

for i in range(1, N+1):
  distance_i = dijkstra(i)
  ans.append(distance_i[X]+distance_X[i])

print(max(ans))