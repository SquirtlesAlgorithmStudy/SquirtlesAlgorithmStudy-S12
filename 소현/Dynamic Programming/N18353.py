# 작성자 : SH_WON_96
# 2021-03-27
# 알고리즘 - DP
# 문제번호 : 18353 병사 배치하기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())

dp = [1]*N
power = list(map(int,fast_in().strip().split()))


"""
15 11 4 8 5 2 4
"""

power.reverse()

for i in range(N): # i = 3 인 경우를 보면
    # i 보다 앞부분을 탐색하는 것. 순서상으로 j , i  가 위치해 있음
    for j in range(i):
        if power[i] > power[j]: #
            dp[i] = max(dp[i], dp[j] + 1) # i번째는 자기 앞에꺼보다 +1
        # 더 크면 감소 안했으니 + 없음

#print(N - max(dp))
print(N - max(dp))


