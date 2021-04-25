# 작성자 : SH_WON_96
# 2021-04-20
# 알고리즘 - DP
# 문제번호 : 11060 점프 점프

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())
A = list(map(int, fast_in().strip().split()))

visited = [float("INF")]*(N)

visited[0] = 0

for i in range(N):
    for j in range(1,A[i]+1):
        if i + j >= N:
            break
        visited[i+j] = min(visited[i+j],visited[i]+1)


if visited[N-1] == float("INF"):
    print(-1)
else:
    print(visited[N-1])