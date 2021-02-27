import sys

N = list(map(int,input().split()))
K = list(map(int,input().split()))
K.sort()

length = N[1]
start = K[0] + length - 1
result = 1

for i in range(1,len(K)):
  if K[i] > start:
    result += 1
    start = K[i] + length - 1

print(result)
