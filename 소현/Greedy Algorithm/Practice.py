# 작성자 : SH_WON_96
# 알고리즘 - Greedy
# 초기 입력값 받기
import sys
input = sys.stdin.readline


# 2021-02-08
# 문제번호 : 1이 될때까지

N,K= map(int,input().split())
count = 0

while N>=K :
    if N % K == 0:
        N = N//K
        count += 1
    else:
        N = N-1
        count += 1

print(count)



# 2021-02-10
# 문제번호 : 큰 수의 법칙
# N 개의 자연수, M개의 수를 더할 것이고, K개의 중복 가능
N,M,K = map(int,input().strip().split())
num = list(map(int,input().strip().split()))
num.sort(reverse=True)

# count = 0
# while M:
#     for i in range(K):
#         if M == 0:
#             break
#         count += num[0]
#         M -= 1
#     if M == 0:
#          break
#     count += num[1]
#     M -= 1
# print(count)

b = M//K # 8//3 = 2
c = M-b*K # 8-2*3

print(num[0]*b*K+num[1]*c)




# 2021-02-10
# 문제번호 : 숫자 카드 게임
N, M = map(int,input().strip().split())

minlist = []
for i in range(N):
    a = list(map(int, input().strip().split()))
    a.sort()
    minlist.append(a[0])

print(max(minlist))