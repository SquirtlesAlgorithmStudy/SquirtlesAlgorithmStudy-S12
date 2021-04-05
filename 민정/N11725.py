import sys
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline()) # node 갯수
nodeGraph = [[] for _ in range(N+1)] # 노드 tree
parents = [0 for _ in range(N+1)] # 부모 노드 저장

for _ in range(N-1):
  i, j = map(int, sys.stdin.readline().split())
  nodeGraph[i].append(j)
  nodeGraph[j].append(i)

print(nodeGraph)

def DFS(Start, Graph, Parents):
  for i in Graph[Start]:
    if Parents[i] == 0:
      Parents[i] = Start
      DFS(i, Graph, Parents)

DFS(1, nodeGraph, parents)
for i in range(2, N+1):
  print(parents[i])

print(parents)