import sys
from collections import deque

N = int(sys.stdin.readline())
listn = deque()

for i in range(N):
    listn.append(i+1)

def card2():
    listn.popleft()
    listn.append(listn[0])
    listn.popleft()

for _ in range(N-1):
    card2()
    
print(listn[0])