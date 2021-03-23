# 작성자 : SH_WON_96
# 2021-03-23
# 알고리즘 - DP
# 문제번호 : 1932 정수 삼각형

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())

nums = []

for _ in range(N):
    nums.append(list(map(int,fast_in().strip().split())))

print(nums)

dp = [[0]*(i+1) for i in range(N)]
dp[0][0] = nums[0][0]

for i in range(1,N):
    #끝은 위에꺼 더하는 방법밖에 없음
    dp[i][0] = dp[i-1][0]+nums[i][0]
    dp[i][i] = dp[i-1][i-1]+nums[i][i]
    # 나머지 좌표들 1~ i 까지
    for j in range(1,i):
        dp[i][j] = (max(dp[i-1][j]+nums[i][j],dp[i-1][j-1]+nums[i][j])) # 같은자리 or 좌측 둘중 max

#print(dp)
print(max(dp[N-1])) # 마지막줄 중 max 값