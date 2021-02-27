import sys

N = int(input())
K = [int(input()) for _ in range(N)]
result = 0
lengthK = len(K)

for i in range(1,lengthK):
  while K[lengthK-i] <= K[lengthK-i-1]:
    result += 1
    K[lengthK-i-1] -= 1

print(result)
