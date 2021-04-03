# 작성자 : SH_WON_96
# 2021-04-02
# 알고리즘 - 이진 탐색
# 문제번호 : 2343 기타 레슨


# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline


N,M = map(int,fast_in().strip().split())

course = list(map(int,fast_in().strip().split()))

start = max(course) # 1개의 영상보다는 블루레이의 크기가 커야함. 그러므로 영상들의 최댓값부터 시작
end = sum(course) # 다 더한것보다는 짧아야지
result = sys.maxsize

# 블루레이의 시간에 대한 이진탐색!
while start <= end:
    mid = (start+end)//2
    if mid < max(course): # mid 값이 max course 보다는 커야함
        start = mid + 1
        continue


    count = 0 # 나뉘어지는 블루레이 갯수
    sumtime = 0 # 누적된 영상시간

    for i in range(len(course)):
        if sumtime + course[i] > mid:
            count += 1
            sumtime = 0
        sumtime += course[i]
    if sumtime:# 맨 뒤에 mid보다 작은 누적된 영상 시간들 체크
        count += 1 #있으면 그것도 블루레이 갯수이지


    if count <= M: # 시간이 너무 짧아서
        result = min(result,mid)
        end = mid - 1
    else:
        start = mid + 1


print(result)

