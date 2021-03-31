# 작성자 : SH_WON_96
# 2021-03-31
# 알고리즘 - DP
# 문제번호 : 11727 2xn 타일링 2

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

n = int(fast_in().strip())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 10007

# 계산된 결과 출력
print(d[n])