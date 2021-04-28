import sys
sys.setrecursionlimit(10 ** 9)
INF = sys.maxsize

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))
Vol = [[0]*(M+1) for _ in range(N+1)]
Vol[0][S] = 1

maxV = S

for i in range(1, N+1):
  for j in range(M+1):
    if Vol[i-1][j] == 0 : continue
    if j-V[i-1]>=0:
      Vol[i][j-V[i-1]] = 1
    if j+V[i-1]<=M:
      Vol[i][j+V[i-1]] = 1
      
maxVol = -1

for i in range(M,-1,-1):
  if Vol[N][i] == 1:
    maxVol = i
    break

print(maxVol)