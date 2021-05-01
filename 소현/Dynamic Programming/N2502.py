# 작성자 : SH_WON_96
# 2021-05-01
# 알고리즘 - DP
# 문제번호 : 2502 떡 먹는 호랑이

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

D,K = map(int, fast_in().strip().split())

# 6일째 41개를 받았으면
# 1일 2개
# 2일 7개
# 3일 (1일 + 2일) = 9개
# 4일 (3일 + 2일) = (1일 + 2일*(1+1))) = 16개
# 5일 (3일 + 4일) = 1일*(1+1)+ 2일*(1+2)= 25개
# 6일 (4일 + 5일) = 1일*(1+2) +2일(2+3) = 41개
# 7일 (5일 + 6일) = 1일*(2+3) + 2일*(3+5) = 66개
# 8일 (6일 + 7일) = 1일*(3+5) + 2일*(5+8) =
# 8일 (6일 + 7일) = 1일*(5+8) + 2일*(8+13) = 66개
# 1 2 3 5 8 13 ---
# N 일차 = 1일 * dp[N-3] + 2일 * dp[N-2]

dp = [0]*30
dp[0] = 1
dp[1] = 2
for i in range(2,30):
    dp[i] = dp[i-2]+dp[i-1]


finish = False

if D > 3:
    for i in range(1,100000):
        for j in range(i+1,100000):
            result = i*dp[D-4] + j*dp[D-3]
            if result == K:
                print(i)
                print(j)
                finish = True
                break
        if finish:
            break
else:
    for i in range(1,100000):
        for j in range(i+1,100000):
            result = i+j
            if result == K:
                print(i)
                print(j)
                finish = True
                break
        if finish:
            break

