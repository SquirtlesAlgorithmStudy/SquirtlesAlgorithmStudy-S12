# 작성자 : SH_WON_96
# 2021-03-29
# 알고리즘 - BFS
# 문제번호 : 11725 트리의 부모 찾기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline
from collections import deque

N = int(fast_in().strip())

treelist = [[] for _ in range(N+1)] # 연결관계 표시해줄 리스트
momlist = [[] for _ in range(N+1)] #

for _ in range(N-1):
    n1,n2 = map(int, fast_in().strip().split())
    treelist[n1].append(n2) # n1과 n2 연결이 있음.
    treelist[n2].append(n1) # 쌍방향으로 다 넣어주기


queue = deque()
momlist[1].append(0) # 1의 mom도 채워주기.
for i in treelist[1]: # 1과 연결된 애들의 mom에 1 넣어주기
    queue.append(i) # 이제 자식들로 bfs 시작할꺼야
    momlist[i].append(1) # 각 자식들의 mom에 넣어주기


def bfs(q,treelist):
    while q:
        x = q.popleft()
        if len(treelist[x])>0: # x에게 자식이 존재한다면
            for i in treelist[x]: # 그 자식들 i
                if len(momlist[i]) == 0 : # 자식들 i에게 mom이 없다면..
                    q.append(i) # 그 자식들도 bfs 돌기
                    momlist[i].append(x) # mom 연결해주기


bfs(queue,treelist)

for sun in momlist[2:]: # 2번째부터 각각의 부모 출력해주기
    print(sun[0])
