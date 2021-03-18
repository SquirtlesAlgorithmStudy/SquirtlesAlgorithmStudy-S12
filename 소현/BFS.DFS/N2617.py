# 작성자 : SH_WON_96
# 2021-03-18
# 알고리즘 - DFS/BFS
# 문제번호 : 2617 구슬 찾기
import sys
fast_in = sys.stdin.readline
sys.setrecursionlimit(10000)
N, M = map(int,fast_in().strip().split())

# 플로이드 와샬로 풀어보기
matrix = [[0]*(N+1) for _ in range(N+1)]
half = N//2

for _ in range(M):
    x, y = map(int, fast_in().strip().split())
    matrix[x][y] = 1 # x가 y 보다 큼
    matrix[y][x] = -1 # y가 x보다 작음

# j 에서 k 를 가는데 만약 i를 거쳐갈 수 있다면 ?  j -> i -> k 이면 감소방향이던 증가방향이던 같은 취급해주면 된다.
for i in range(1,N+1): # 거쳐가는 구슬 i
    for j in range(1,N+1): # 출발 구슬
        for k in range(1,N+1): #도착 구슬
            # 출발구슬 -> 거쳐가는 구슬, 거쳐가는 구슬 -> 도착 구슬
            # 이렇게 정렬이 되면 출발 구슬 -> 도착 구슬이 만들어질 수 있음.
            if matrix[k][i] != 0 and matrix[j][i] == matrix[i][k] : # 값이 0 이 아니고 출발- 거쳐, 거쳐 - 도착이 같은 방향(+ or -) 이면
                matrix[j][k] = matrix[j][i] # 출발 - 도착도 같은 방향으로 연결된다.


big = [0]*(N+1)
small = [0]*(N+1)

for i in range(1,N+1):
    for j in range(1,N+1):
        # i 보다 큰수들의 갯수는 big에 저장하고, 작은 수들의 갯수는 small에 저장함
        if matrix[i][j] == 1:
            big[i] += 1
        if matrix[i][j] == -1:
            small[i] += 1

total = 0

for i in range(1,N+1): #그래서 i라는놈보다 작은수 또는 큰수들의 갯수가 절반 이상이라면 i는 가운데에 올 수 없음
    if big[i] > half : total += 1
    if small[i] > half : total += 1

print(total)

# 내가 처음에 짠 코드는 실패. 순차적으로 탐색하는데 약간 뭔가 꼬인듯
"""
stone = [[set([]),set([])] for _ in range(N+1)]



#def updatelight(s,l,v):
def update(s,l,v):
    # 나(l)한테 무거운 것이 추가되었을 때, 나 = 가벼운 애
    # 나보다 가벼운애한테 무거운 값 넣어주기 + 나보다 가벼운 애들을 무거운 애한테 없으면 넣어주기
    if len(stone[l][0])>0: # 나보다 가벼운 것이 있으면
        for i in stone[l][0]: # 가벼운 애들(i)
            if v not in stone[i][1]: # 가벼운 애들의 무거운 값들에 v가 없으면 넣어주기
                stone[i][1].add(v)
                update(stone,i,v) # 가벼운 i에게 v를 넣어준 상황
            if i not in stone[v][0]: # 나보다 가벼운 애들을 나보다 무거운 v 에게 넣어주기
                stone[v][0].add(i)
                update(stone,i,v) # 가벼운 i를 v에

    # 나(v)한테 가벼운 것이 추가되었을 때, 나 = 무거운 애
    # 나보다 무거운 애한테 가벼운 값 넣어주기, 나보다 무거운애들을 가벼운 애한테 없으면 넣어주기
    if len(stone[v][1]) > 0: # 나보다 무거운 것들이 있으면
        for i in stone[v][1]: # 무거운 애들(i)
            if l not in stone[v][0]: # 무거운 애들이 l가 없으면
                stone[v][0].add(l) # l 넣어주기
                update(stone,l,i) # 무거운 i 에게 가벼운 l
            if i not in stone[l][1]: # 나보다 무거운 애들을 나보다 가벼운 l의 [1]에 넣어주기
                stone[l][1].add(i)
                update(stone,l,i)



# 내꺼 무게랑, 나를 참고하고 있는 애들을 리스트로 받아야함. # 무게는 나보다 작은 애들의 갯수인 거고, 참고하고있는 리스트 크기는 나보다 큰 애들인 거임.
# [[[앞리스트1], [뒤리스트1]], [[앞리스트2], [뒤리스트2]], [[앞리스트3], [뒤리스트3]] ]
for _ in range(M):
    heavy , light =  map(int,fast_in().strip().split())
    stone[heavy][0].add(light) # heavy입장에서는 가벼운 것 추가
    stone[light][1].add(heavy) # light입장에서는 무거운 것 추가

    update(stone,light,heavy) #




stone = stone[1:] # 헷갈리니까 첫번째꺼 없애고...
total = 0
for i in range(N):
    if len(stone[i][0]) > N//2 :
        total += 1
    elif len(stone[i][1]) > N//2:
        total += 1

print(total)

"""
# 이건 dfs를 이용한 코드...
"""
def solve():
    n, m = map(int, sys.stdin.readline().strip().split())
    heavier = [[] * (n + 1) for _ in range(n + 1)]
    lighter = [[] * (n + 1) for _ in range(n + 1)]
    mid = n // 2

    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        heavier[v2].append(v1)
        lighter[v1].append(v2)

    def dfs(now, path):
        visited = [False] * (n + 1)
        stack = [now]
        visited[now] = True
        cnt = 0
        while stack:
            now = stack.pop()
            for next in path[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                    cnt += 1
                    if cnt > mid:
                        return 1
        return 0

    answer = 0
    for i in range(1, n + 1):
        answer += dfs(i, heavier)
        answer += dfs(i, lighter)
    return answer
    
print(solve())


"""


