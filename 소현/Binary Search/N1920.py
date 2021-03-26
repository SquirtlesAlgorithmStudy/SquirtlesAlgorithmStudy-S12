# 작성자 : SH_WON_96
# 2021-03-26
# 알고리즘 - 이진탐색
# 문제번호 : 1920 수 찾기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())
a = list(map(int, fast_in().strip().split()))
M = int(fast_in().strip())
b = list(map(int, fast_in().strip().split()))

def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

a.sort()

for x in b :
    if binary_search(a,x,0,len(a)-1) == None:
        print(0)
    else:
        print(1)

