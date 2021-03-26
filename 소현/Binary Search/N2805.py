"""# 작성자 : SH_WON_96
# 2021-03-26
# 알고리즘 - 이진탐색
# 문제번호 : 2805 나무 자르기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N,M = map(int, fast_in().strip().split())


treelist = list(map(int, fast_in().strip().split()))

start = 0
end = max(treelist)
mid = end//2
result = 0

while start <= end:
    total = 0 # 현재 기준에서 잘려진 떡들의 합
    mid = (start + end)//2 # 자르는 위치

    total = sum([x - mid for x in treelist if x > mid])

    if total < M: # 잘랐더니 원하는 양보다 적다면 끝점을 더 가운데로 당겨야함
        end = mid - 1 # 그래서 mid - 1 로 옮겨왔쥐
    else:
        result = mid # 일단 mid로 잘라도 ㅇㅋ 근데 좀 남을꺼임
        start = mid + 1 # 남는걸수도 있으니까 mid + 1 로 넘어가서 더 뒤쪽을 잘라보자


print(result)"""

import sys
from collections import Counter
def cut_tree(trees,std):
    sum=0
    for tree, cnt in trees.items(): # {20: 1, 15: 1, 10: 1, 17: 1}
        if tree > std:
            sum+=(tree-std)*cnt

    return sum

N, M = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.readline().split())) # Counter 는 인자로 받은 배열의 값이 몇개 있는지 반환해준다. Dictionary 구조로 바꿔줌.
#print(trees) # 반환 결과 보기
s,e=0,max(trees)

while s<=e:
    mid=(s+e)//2

    if cut_tree(trees,mid) >= M:
        s=mid+1
    else:
        e=mid-1

print(e)