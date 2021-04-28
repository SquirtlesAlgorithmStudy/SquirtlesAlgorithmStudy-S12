# 작성자 : SH_WON_96
# 2021-04-28
# 알고리즘 - BFS
# 문제번호 : 5567 결혼식

# 초기 입력값 받기
import sys
from collections import deque
fast_in = sys.stdin.readline

N = int(fast_in().strip())
m = int(fast_in().strip())

connection = [[] for _ in range(N+1)]
visited = [0]*(N+1)
stnum = [i for i in range(1,N+1)]

for _ in range(m):
    a,b = map(int, fast_in().strip().split())
    connection[a].append(b)
    connection[b].append(a)

# 상근이 친구의 친구까지 초대

queue = deque([])
visited[1] = 1
for a in connection[1]:
    queue.append(a)
    visited[a] = 1

while queue:
    x = queue.popleft()

    for a in connection[x]:
        visited[a] = 1


print(sum(visited)-1)