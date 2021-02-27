# 작성자 : SH_WON_96
# 2021-02-26
# 알고리즘 - 자료구조, 스택
# 문제번호 : 카드2

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

queue = deque(list(range(1,N+1)))

while len(queue) != 1:
    pop1 = queue.popleft()
    if len(queue)== 1:
        break
    pop2 = queue.popleft()
    queue.append(pop2)

print(queue.pop())

"""
queue[1::2] - > 1부터 2간격으로 슬라이싱한 결과

queue = list(range(1,N+1))

while len(queue) != 1:
    if len(queue)%2 == 1:
        newq = (queue[1::2])
        newq.insert(0,queue[-1])
        queue = (newq)
    else:
        queue = queue[1::2]

print(queue[0])

"""