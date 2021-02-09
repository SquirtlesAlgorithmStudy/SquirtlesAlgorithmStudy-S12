# 작성자 : SH_WON_96
# 2021-02-08
# 알고리즘 - Greedy
# 문제번호 : 1439 뒤집기

# 초기 입력값 받기
import sys
input = sys.stdin.readline

N = [i for i in input().strip()]

num = N[0]
tmp = [num]

for i in range(1,len(N)):
    if N[i] == tmp[-1]:
        num = N[i]
    else:
        tmp.append(N[i])
        num = N[i]

print(tmp)


s = sum(list(map(int,tmp)))

if len(tmp)==1:
    print(0)
elif s > len(tmp)-s :
    print(len(tmp)-s)
else:
    print(s)