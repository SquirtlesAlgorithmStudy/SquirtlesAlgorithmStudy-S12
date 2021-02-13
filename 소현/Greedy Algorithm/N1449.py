# 작성자 : SH_WON_96
# 2021-02-13
# 알고리즘 - Greedy
# 문제번호 : 1449 수리공 항승

# 초기 입력값 받기
import sys
input = sys.stdin.readline

# 물 새는 위치 N , 테이프 길이 L
N, L = map(int,input().split())
tmp = list(map(int,input().split()))

# L-1 길이만큼 커버 가능.
count = 0
tmp.sort()
i = 0
while i < N :
    until = 0
    for j in range(i+1,N):
        if tmp[j]-tmp[i] <= L-1:
            until += 1
    i += until+1

    count += 1

print(count)