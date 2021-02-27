import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
dq = deque([i for i in range(n, 0, -1)])

while len(dq) != 1:
  dq.pop()
  dq.appendleft(dq[len(dq)-1])
  dq.pop()

print(dq[0])
 





