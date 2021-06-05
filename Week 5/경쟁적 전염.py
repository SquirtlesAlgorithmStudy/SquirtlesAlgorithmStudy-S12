from operator import itemgetter
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
queue = deque()
graph = [list(map(int, input().strip().split())) for _ in range(n)]
s, x, y = map(int, input().strip().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(queue):
    global s
    past_t = -1
    t = 0
    while queue:
        if past_t < t : queue = deque(sorted(queue, key = itemgetter(3)))
        t, x, y, virus = queue.popleft()
        past_t = t
        if t == s: break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue
            if graph[nx][ny] == 0  :
                graph[nx][ny] = virus
                queue.append((t + 1, nx, ny, virus))
               

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((0, i, j, graph[i][j]))

bfs(queue)
print(graph[x - 1][y - 1])