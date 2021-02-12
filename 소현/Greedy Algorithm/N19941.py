# 작성자 : SH_WON_96
# 2021-02-12
# 알고리즘 - Greedy
# 문제번호 : 19941 햄버거

# 초기 입력값 받기
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

table = list(input().strip())
#print(table)

count = 0

for i in range(N):
    if(table[i]=="P"):
        for j in range(i-K,i+K+1):
            if j>=0 and j<N and table[j]=="H" :
                # 햄버거 먹으면 햄버거 지워버리기
                table[j] = ""
                count += 1
                break

print(count)