import sys
sys.setrecursionlimit(1000000)
fastin = sys.stdin.readline
n = int(fastin())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  l,m = map(int,fastin().strip().split())
  graph[l].append(m)
  graph[m].append(l)
visited = [0] * (n+1)
cnt = 0

def dfs(node, visited):
  global cnt
  cnt += 1
  if visited[node] != 0 :
    cnt -= 1
    return 0
  visited[node] = cnt
  for i in graph[node]:
    dfs(i, visited)
  cnt-=1
  return 0

dfs(1, visited)
for i in range(n-1):
  if len(graph[i+2]) == 1: print(graph[i+2][0])
  elif 1 in graph[i+2] : print(1)
  else : 
    for j in graph[i+2]:
      if visited[j] == visited[i+2] - 1 : 
        print(j)
        break