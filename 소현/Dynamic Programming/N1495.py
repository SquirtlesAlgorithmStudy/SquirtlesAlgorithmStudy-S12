# 작성자 : SH_WON_96
# 2021-04-20
# 알고리즘 - DP
# 문제번호 : 1495 기타리스트

# 초기 입력값 받기
"""
import sys
fast_in = sys.stdin.readline

N, S, M = map(int, fast_in().strip().split()) # 곡의 갯수 N , 시작 볼륨 S, max M
V = [0]+list(map(int,fast_in().strip().split()))
# 현재볼륨(i-1)번째 P, i 번째 곡이면 P+-V[i]

# 3 5 10
# 5 3 7

# 0 번째
# 1번째 : 5-5 / 5 + 5
# 2번째 : 5-3 / 5 + 3
# 3번째 :

dp = [[0,0] for _ in range(N+1)]
dp[0] = [S,S]


result = False

for i in range(1,N+1):
    # 4가지 경우
    v1 = dp[i - 1][0] - V[i] # 제일 작고
    v2 = min(dp[i - 1][0] + V[i],dp[i - 1][1] - V[i]) # 2랑 3은 알 수 없으니깐 순서대로 넣어주기
    v3 = max(dp[i - 1][0] + V[i],dp[i - 1][1] - V[i])
    v4 = dp[i - 1][1] + V[i] # 제일 크고


    if 0 <= v1 <= M:
        dp[i][0] = v1
        if v4 <= M:
            dp[i][1] = v4
        elif v3 <= M :
            dp[i][1] = v3
        elif v2 <= M:
            dp[i][1] = v2
        else:
            dp[i][1] = v1

    elif 0<= v2 <= M :
        dp[i][0] = v2
        if v4 <= M:
            dp[i][1] = v4
        elif v3 <= M:
            dp[i][1] = v3
        else:
            dp[i][1] = v2

    elif 0<= v3 <= M :
        dp[i][0] = v3
        if v4 <= M:
            dp[i][1] = v4
        else:
            dp[i][1] = v3

    elif 0 <= v4 <= M:
        dp[i][0] = v4
        dp[i][1] = v4

    else:
        result = True
        break


if result:
    print(-1)
else:
    print(dp[N][1])
"""

import sys
input = sys.stdin.readline

n, start, max_v = map(int, input().split())
v = list(map(int, input().split()))

dp = []
for _ in range(n+1):
    dp_arr = [False] * (max_v + 1)
    dp.append(dp_arr)
dp[0][start] = True

for i in range(n):
    for j in range(max_v+1):
        check = dp[i][j]
        if check:
            if j + v[i] <= max_v:
                dp[i+1][j+v[i]] = True
            if j - v[i] >= 0:
                dp[i+1][j-v[i]] = True

result = -1
for i in range(max_v+1):
    if dp[n][i]:
        result = i
print(result)


