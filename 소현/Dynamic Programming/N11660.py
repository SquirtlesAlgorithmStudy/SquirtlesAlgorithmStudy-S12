# 작성자 : SH_WON_96
# 2021-03-21
# 알고리즘 - DP
# 문제번호 : 11660 구간합 구하기 5

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N,M = map(int,fast_in().strip().split())

matrix = [[0]*(N+1)]

for _ in  range(N):
    matrix.append([0]+list(map(int,fast_in().strip().split())))

dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = matrix[1][1]
# for i in range(1,N+1):
#     dp[i][1] = dp[i-1][1]+matrix[i][1]
#     dp[1][i] = dp[1][i-1]+matrix[1][i]


for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i][j]

for case in range(M):
    x1,y1,x2,y2 = map(int,fast_in().strip().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])