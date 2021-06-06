from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 같은 학번 (노드수)
m = int(input()) # 친구 관계 여부 (간선수))
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
# 시작 노드 포함 n번째 노드까지 거치는 총 노드 갯수
cnt = 0

def bfs(G, V, start):
  queue = deque()
  V[start] = 1
  queue.append(start)
  while queue:
    num = queue.popleft()
    for i in range(1,n+1):
      if V[i] == 0 and G[num][i] == 1:
        queue.append(i)
        V[i] = V[num]+1
  return V

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

visited = (bfs(graph, visited, 1))
print(visited)

# 친구의 친구까지 됨
# 즉 (시작)~(친구)~(친구의 친구); 방문 노드수 3개 이하여야 초대 가능
for i in range(2,n+1): # 0이랑 1번(나)은 제외해야됨
  if visited[i]<=3 and visited[i]>0: cnt+=1

print(cnt)