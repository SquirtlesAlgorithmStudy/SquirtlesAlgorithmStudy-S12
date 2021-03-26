# 작성자 : SH_WON_96
# 2021-03-23
# 알고리즘 - DP
# 문제번호 : 14501 퇴사

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())
table = []
dp = []

for i in range(N):
    t,p = map(int,fast_in().strip().split())
    table.append([t,p])
    dp.append(p)

dp.append(0)
print(table)
print(dp)

for i in range(N-1,-1,-1):
    t = table[i][0]
    p = table[i][1]
    if t + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],p+dp[i+t])

print(dp[0])