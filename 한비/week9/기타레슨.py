import sys
input=sys.stdin.readline


def add_lesson():
    cnt = 0  # 레코드 갯수 세기
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합
    for i in range(N):
        if sum_lesson + lesson_list[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lesson_list[i] #두번째값 업데이트
    else:
        if sum_lesson:
            cnt += 1
    return cnt

N, M = map(int, input().split())  # N: 레슨 수, M: 블루레이 수
lesson_list = list(map(int, input().split()))  

right = sum(lesson_list)  
left = max(lesson_list)  
while left <= right:
    mid = (left + right) // 2
    cnt = add_lesson()
    if cnt <= M:  
        right = mid - 1
    elif cnt > M: 
        left = mid + 1


print(left)