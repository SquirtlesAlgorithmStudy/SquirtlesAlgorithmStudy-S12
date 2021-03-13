from collections import deque
 
n = int(input())
graph = []
max = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max:
            max = graph[i][j]
            
def bfs(i, j, value, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
   
maximum = 0
for a in range(max):
    visited = [[0] * n for _ in range(n)] 
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > a and visited[i][j] == 0: 
                bfs(i, j, a, visited)
                ans += 1
    if maximum < ans:
        maximum = ans
print(maximum)