# 작성자 : SH_WON_96
# 2021-03-21
# 알고리즘 - back tracking
# 문제번호 : 15650 N과 M

# 초기 입력값 받기
import sys
from itertools import combinations
fast_in = sys.stdin.readline

N,M = map(int, fast_in().strip().split())

nums = [i for i in range(1,N+1)]

for num in list(combinations(nums,M)):
    print(" ".join((str(i) for i in num)))
