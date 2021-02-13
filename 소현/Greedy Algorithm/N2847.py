# 작성자 : SH_WON_96
# 2021-02-13
# 알고리즘 - Greedy
# 문제번호 : 2847 게임을 만든 동준이

# 초기 입력값 받기
import sys
input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))


count = 0
#num[i]랑 num[i-1] 비교해서 작게 만들어야함.
for i in range(1,N):
    if num[N-i-1] >= num[N-i]:
        val = num[N-i-1]-num[N-i]
        count += val+1
        num[N-i-1] = num[N-i-1]-val-1

print(count)