# 작성자 : SH_WON_96
# 2021-03-16
# 알고리즘 - Sort
# 문제번호 : 18310 안테나

import sys

fast_in = sys.stdin.readline

N = int(fast_in().strip())


house = []

for i,t in enumerate(fast_in().strip().split()):
    house.append([i,int(t)])


house.sort(key= lambda x : x[1])

def caldist(h,a):
    sumup = 0
    for t in h:
        sumup += abs(a-t[1])

    return sumup

if N %2 == 0:
    if caldist(house,house[N//2-1][1]) <= caldist(house,house[N//2][1]):
        print(house[N//2-1][1])
    else:
        print(house[N//2][1])
else:
    print(house[N//2][1])


"""
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[(n-1)//2])

사실 그냥 정렬해서 가운데값 가져오면 되는거니깐
"""