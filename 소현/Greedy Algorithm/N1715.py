# 작성자 : SH_WON_96
# 2021-02-13
# 알고리즘 - Greedy
# 문제번호 : 1715 카드 정렬하기

# 초기 입력값 받기
import sys
from queue import PriorityQueue
import heapq
input = sys.stdin.readline

N = int(input())

# queue = PriorityQueue()
# for i in range(N):
#     queue.put(int(input()))


# 10, 20 , 40 이면
count = 0
# while queue.qsize()!=1:
#     num1 = queue.get()
#     num2 = queue.get()
#     newnum = num1 + num2
#     queue.put(newnum)
#     count += newnum

heap = []
for i in range(N):
    heapq.heappush(heap,int(input()))

while len(heap)!=1 :
    num = heapq.heappop(heap)+heapq.heappop(heap)
    count += num
    heapq.heappush(heap,num)

print(count)