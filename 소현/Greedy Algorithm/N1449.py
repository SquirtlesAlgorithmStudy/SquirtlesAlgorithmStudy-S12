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

count = 0 # 사용될 테이프 갯수
tmp.sort() # 순서대로 탐색할꺼니 정렬
i = 0 # 탐색 idx

while i < N :
    until = 0 # i 부터 어디까지 커버가능한지 체크한 후 until 다음꺼부터 다시 탐색하는 과정
    for j in range(i+1,N):
        # L-1 길이만큼 커버 가능하고 until로 몇번째 인덱스까지 커버인지 체크
        if tmp[j]-tmp[i] <= L-1:
            until += 1
    # until 다음으로 이동
    i += until+1
    # i~ until까지 덮는 테이프 1개 추가
    count += 1

print(count)