# p[k] : 카드 k개 들은 카드팩 가격
# dp[i] : 카드 i개 구매하는 최대 가격
# (i>k)

# dp[1] = 1
# dp[2] = 2  :  dp[2]*1, dp[1]*2
# dp[3] = 3  :  dp[3]*1, dp[1]+dp[2]
# dp[4] = 4  :  dp[4]*1, dp[1]+dp[3], dp[2]*2
# i개를 구매할 때 최대 가격이 나오는 점화식 : dp[i] = p[k] + dp[i-k]
# 그럼 p[i]랑 dp[i-k]+p[k] 둘 중에 큰걸 비교하면됨

N = int(input())
p = [0] + list(map(int, input().split()))
dp = [0] * (N+1)

for i in range(1, N+1):
  for k in range(1, i+1):
    dp[i] = max(dp[i], dp[i-k]+p[k])

print(dp[N])