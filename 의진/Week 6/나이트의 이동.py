from collections import deque
import sys
input = sys.stdin.readline

  
def bfs(start, goal, visited):
    queue = deque([])
    queue.append(start)
    cnt = 0
    x, y = start
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        if visited[x][y] == cnt: cnt += 1

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l:
                if [nx, ny] == goal: return cnt
                if visited[nx][ny] == -1: 
                  visited[nx][ny] = cnt
                  queue.append([nx, ny])

t = int(input().strip())
result = []
for _ in range(t):
    l = int(input().strip())
    start = list(map(int, input().strip().split()))
    goal = list(map(int, input().strip().split()))
    if goal == start :
      result.append(0)
      continue
    visited = [[-1] * l for _ in range(l)]
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    a = bfs(start, goal, visited)
    result.append(a)

for i in range(t):
    print(result[i])
