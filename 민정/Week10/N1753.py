# NO 플로이드
# "특정" 노드 출발 >> 다른 모든 노드로 가는 최단 경로 계산
# 다익스트라 사용 (이코테 30강) : 매상황 가장 비용이 적은 노드를 선택
# heapq : 최소힙

import sys
import heapq
sys.setrecursionlimit(10 ** 9)

INF = sys.maxsize

V, E = map(int, sys.stdin.readline().split()) # 정점, 간선(가중치)
W = int(sys.stdin.readline()) # 출발점

dist = [INF] * (V+1)
graph = [[] for _ in range(V+1)]
heap = [] # 최소 힙을 위한 큐

for _ in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  if c > 10 : continue # w
  else : graph[a].append((b,c))

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

dijkstra(W)

for i in range(1, V+1):
  if dist[i] == INF:
    print("INF", end = " ")
  else : print(dist[i], end = " ")
print()