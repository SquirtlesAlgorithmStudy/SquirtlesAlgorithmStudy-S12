import sys
input=sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
ans = 0
while high >= low:
    pivot = int((low+high)/2)
    sum_tree = sum([x - pivot if x >= pivot else 0 for x in trees])
    # 비교
    if sum_tree >= M:
        low = pivot + 1
        if ans < pivot: 
            ans = pivot
    elif sum_tree < M: 
        high = pivot - 1

print(ans)