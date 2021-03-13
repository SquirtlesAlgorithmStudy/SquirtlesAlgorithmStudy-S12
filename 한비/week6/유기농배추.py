from collections import deque 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j, visited):
    count = 0
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count += 1
    while q:
        x, y = q.popleft()
        for i in range(5):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx,ny))

    return count
                                
t = int(input())
for _ in range(t):
    m, n, k = list(map(int, input().split(' ')))
    arr = [[[0] for _ in range(m)] for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    for _ in range(k):
        x, y = map(int, input().split(' '))
        arr[y][x] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == False:
                  ans += bfs(i, j, visited)      
    print(ans)