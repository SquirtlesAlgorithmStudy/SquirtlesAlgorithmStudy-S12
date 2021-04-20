import sys
fastin = sys.stdin.readline

import heapq
inf = 10**9
n,e = map(int,fastin().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a,b,c = map(int,fastin().split())
  graph[a].append((b,c))
  graph[b].append((a,c))


v1, v2 = map(int,fastin().split()) 

def dis(start, finish):
  q = []
  distance = [inf] * (n+1)
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
  return distance[finish]      

d = []
d.append(dis(1, v1)) #0
d.append(dis(1, v2)) #1
d.append(dis(1, n))  #2
d.append(dis(v1, v2))#3
d.append(dis(v1, n)) #4
d.append(dis(v2, n)) #5

res = min(
  d[0] + d[3] + d[5],
  d[1] + d[3] + d[4],
  d[0] + 2 * d[3] + d[4],
  d[1] + 2 * d[3] + d[5],
  d[0] + d[3] + d[1] + d[2],
  2 * d[0] + d[1] + d[5],
  2 * d[1] + d[0] + d[4]
)

  
if res >= inf : print(-1)
else: print(res)


# inf 값이 오버플로우가 날 수 있음을 주의해야함 !!!
# 사실 이 문제에서 문제 조건 범위가 한정되있어서 잘 나온거지
# 실제로는 이동 불가인 것을 더 잘 처리해주어야함