# 작성자 : SH_WON_96
# 2021-03-22
# 알고리즘 - back tracking
# 문제번호 : 15654 N과 M (5)

import sys
from itertools import permutations
fast_in = sys.stdin.readline

N,M = map(int, fast_in().strip().split())
nums = list(map(int,fast_in().strip().split()))
nums.sort()

#result = sorted(result)
for num in list(permutations(nums,M)):
    print(" ".join((str(i) for i in num)))
