# 작성자 : SH_WON_96
# 2021-03-23
# 알고리즘 - DP
# 문제번호 : 2407 조합

import sys
fast_in = sys.stdin.readline

N,M = map(int, fast_in().strip().split())


pecto = [1]*101

for i in range(1,101):
    pecto[i] = pecto[i-1]*i

print(pecto[N]//pecto[N-M]//pecto[M])