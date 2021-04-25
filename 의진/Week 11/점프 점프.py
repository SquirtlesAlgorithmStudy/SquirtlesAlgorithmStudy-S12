'''
다익스트라로 구현 But 시간 초과
import sys
fastin = sys.stdin.readline
import heapq
inf = 10 ** 9

n = int(fastin())
maze = [0] + list(map(int, fastin().split()))

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, maze[i]+1):
    if (i + j) <= n:
      graph[i].append(i+j)

def jump():
  jumplist = [inf] * (n+1)
  jumplist[1] = 0
  q = []
  q.append((jumplist[1], 1))

  while q:
    jumps, now = heapq.heappop(q)
    if jumplist[now] < jumps : continue
    for i in graph[now]:
      if jumplist[i] > jumps :
        jumplist[i] = jumps + 1
        heapq.heappush(q, (jumplist[i], i))
  if jumplist[n] == inf : return -1
  return jumplist[n]

print(jump())
'''
import sys
fastin = sys.stdin.readline


n = int(fastin())
maze = list(map(int, fastin().split()))

d = [0]
for i in range(1, n):
  min_list = []
  for j in range(i):
    if (d[j] != -1) and (j + maze[j] >= i) :
      min_list.append(d[j])
  if len(min_list) == 0 : d.append(-1)
  else: d.append(min(min_list)+1)
print(d[n-1])