import sys
import heapq
fastin = sys.stdin.readline
inf = 10 ** 9

n, m ,x = map(int, fastin().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, fastin().split())
  graph[a].append((c, b))

def times(start, finish):
  q = []
  timelist = [inf] * (n+1)
  timelist[start] = 0
  q.append((timelist[start], start))

  while q:
    t, node = heapq.heappop(q)
    if timelist[node] < t : continue
    for i, j in graph[node]:
      if timelist[j] > t + i:
        timelist[j] = t + i
        heapq.heappush(q, (timelist[j], j))
  return timelist[finish]

result = []  
for i in range(n):
  if i+1 != x:
    heapq.heappush(result, -(times(i+1, x) + times(x, i+1)))
print(-result[0])