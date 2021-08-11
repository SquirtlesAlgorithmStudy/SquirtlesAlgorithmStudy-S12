## [2164] 카드2
from collections import deque
queue = deque()

n=int(input())

#1~n 원소 넣은 큐 만들기
for i in range(n):
  queue.append(i+1)

while len(queue)!=1:
  queue.popleft()
  queue.append(queue[0])
  queue.popleft()

print(queue[0])