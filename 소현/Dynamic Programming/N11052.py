# 작성자 : SH_WON_96
# 2021-03-31
# 알고리즘 - DP
# 문제번호 : 11052 카드 구매하기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline
N = int(fast_in().strip())

price = [0] + list(map(int, fast_in().strip().split()))

dp = price.copy()

dp[1] = price[1]
dp[2] = max(price[2],price[1]*2)
for i in range(1,N+1):
    for j in range(1,i):
        dp[i] = max(dp[i],dp[i-j]+dp[j])


print(dp[N])