# 작성자 : SH_WON_96
# 2021-04-02
# 알고리즘 - 이진 탐색
# 문제번호 : 2343 기타 레슨


# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline


N,M = map(int,fast_in().strip().split())

course = list(map(int,fast_in().strip().split()))

start = max(course)
end = sum(course)
result = sys.maxsize

# 블루레이의 시간에 대한 이진탐색!
while start <= end:
    mid = (start+end)//2
    if mid < max(course):
        start = mid + 1
        continue

    count = 0
    sumtime = 0
    for i in range(len(course)):
        if sumtime + course[i] > mid:
            count += 1
            sumtime = 0
        sumtime += course[i]
    if sumtime:
        count += 1


    if count <= M: # 시간이 너무 짧아서
        result = min(result,mid)
        end = mid - 1
    else:
        start = mid + 1


print(result)

