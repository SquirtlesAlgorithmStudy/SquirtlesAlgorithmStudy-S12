
#답은 맞으나, 시간초과
import sys
N=int(sys.stdin.readline())
li=[i+1 for i in range(N)]

top=0
while len(li)>1:
    li.remove(li[0])
    v=li.pop()
    li.append(v)
print(li[0])

#디큐 이용
from collections import deque
import sys
N=int(sys.stdin.readline())

dq = deque(range(1,N+1))
    
while len(dq)>1:
    dq.remove(dq[0])
    v=dq.popleft()
    dq.append(v)

print(dq[0])

