import sys
from collections import deque

input=sys.stdin.readline

def bfs(start):
    q = deque([start])

    while q:
        parent = q.popleft()
        for child in graph[parent]:
            if not visited[child]:
                visited[child] = parent
                q.append(child)

    print('\n'.join(map(str, visited[2:])))



n = int(input())
visited = [0] * (n + 1)
visited[1] = 1
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node, connect = map(int, input().split())
    graph[node].append(connect)
    graph[connect].append(node)

bfs(1)