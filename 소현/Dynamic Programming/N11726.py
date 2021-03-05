# 작성자 : SH_WON_96
# 2021-03-05
# 알고리즘 - DP
# 문제번호 : 11726 2*n 타일링

import sys
fast_in = sys.stdin.readline

n = int(fast_in().strip())

s = [0, 1, 2]
for i in range(3, n+1):
  s.append(s[i - 2] + s[i - 1])

print(s[n] % 10007)