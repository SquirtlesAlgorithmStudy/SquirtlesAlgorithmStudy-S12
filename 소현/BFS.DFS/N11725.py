# 작성자 : SH_WON_96
# 2021-03-29
# 알고리즘 - BFS
# 문제번호 : 11725 트리의 부모 찾기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline
from collections import deque

N = int(fast_in().strip())

treelist = [[] for _ in range(N+1)]
momlist = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1,n2 = map(int, fast_in().strip().split())
    treelist[n1].append(n2) # n1 - n2 연결이 있음.
    treelist[n2].append(n1)


queue = deque()
momlist[1].append(0)
for i in treelist[1]:
    queue.append(i)
    momlist[i].append(1)


def bfs(q,treelist,mom):
    while q:
        x = q.popleft() # from, to
        if len(treelist[x])>0:
            for i in treelist[x]:
                if len(momlist[i]) == 0 :
                    q.append(i)
                    momlist[i].append(x)




bfs(queue,treelist,momlist)
for sun in momlist[2:]:
    print(sun[0])
