# 작성자 : SH_WON_96
# 2021-04-03
# 알고리즘 - back tracking
# 문제번호 : 15654 N과 M (4)

import sys
from itertools import combinations_with_replacement
fast_in = sys.stdin.readline

N,M = map(int, fast_in().strip().split())

nums = [i for i in range(1,N+1)]

for num in list(combinations_with_replacement(nums,M)):
    print(" ".join((str(i) for i in num)))
