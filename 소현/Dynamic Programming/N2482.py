# 작성자 : SH_WON_96
# 2021-04-27
# 알고리즘 - DP
# 문제번호 : 2482 색상환

# 초기 입력값 받기
import sys
sys.setrecursionlimit(10**9)
fast_in = sys.stdin.readline

# 원순열?

N = int(fast_in().strip())
K = int(fast_in().strip())
result = 0

dp = [[0]*(N+1) for _ in range(N+1)] #  N숫자ㅇ서 k를 찾는 건가? 살려줘

def find(n,k,dp):
    if n/k == 2:
        return 2
    if k == 1:
        return n
    if dp[n][k] == 0:
        tmp = find(n-2,k-1,dp) + find(n-1,k,dp)
        dp[n][k] = tmp
        return tmp
    else:
        return dp[n][k]

if N/K <2:
    print(0)
else:
    print(find(N,K,dp)%1000000003)
