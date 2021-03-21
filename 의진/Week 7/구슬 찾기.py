import sys 
input = sys.stdin.readline

n, m = map(int,input().strip().split())
graph_1 = [[] for _ in range(n+1)]
graph_2 = [[] for _ in range(n+1)]

for _ in range(m):
  i, j = map(int,input().strip().split())
  graph_1[i].append(j)
  graph_2[j].append(i)


def dfs(graph, v):
  global cnt
  global res
  global visited
  visited[v] = 1

  for i in graph[v]:
    if visited[i] == 0: 
     cnt+=1
     if cnt == (n//2+1):
       res += 1
       return 0
     dfs(graph, i)
  return 0  

res = 0
for i in range(1, n+1):
  cnt = 0
  visited = [0] * (n+1)
  dfs(graph_1, i)

for i in range(1, n+1):
  cnt = 0
  visited = [0] * (n+1)
  dfs(graph_2, i)
print(res)