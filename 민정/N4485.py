# 도둑 루피 = 가중치
# 제일 적은 루피가 있는 곳을 따라가야됨
# 배열로 입력을 받음, dist는 2차원 배열로

import sys
import heapq
sys.setrecursionlimit(10 ** 9)

INF = sys.maxsize
cnt = 0
dx = (-1,0,1,0)
dy = (0,1,0,-1)

def dij(graph, dist, n):
  heap = []
  heapq.heappush(heap, (0, 0, 0))
  dist[0][0] = 0
  while heap:
    d, x, y = heapq.heappop(heap)
    if dist[x][y] < d: continue
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx<0 or nx>=n or ny<0 or ny>=n: continue
      nd = d + graph[nx][ny]
      if dist[nx][ny] > nd:
        dist[nx][ny] = nd
        heapq.heappush(heap, (nd, nx, ny))
  return dist[n-1][n-1] + graph[0][0]

while True :
  cnt += 1
  N = int(sys.stdin.readline())
  if N == 0 : break
  graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  distance = [[INF]*(N+1) for _ in range(N+1)]
  print("Problem %d:"%cnt, dij(graph, distance, N))