# 작성자 : SH_WON_96
# 2021-03-05
# 알고리즘 - DP
# 문제번호 : 9461 파도반 수열

import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())


def checker(p):
    dp = [1,1,1,2,2]
    if p >4:
        for i in range(5,p):
            dp.append(dp[i-5]+dp[i-1])

    return dp[p-1]

for i in range(N):
    print(checker(int(fast_in().strip())))
