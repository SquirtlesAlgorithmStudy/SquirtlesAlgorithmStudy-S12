import sys
fastin = sys.stdin.readline
n = int(fastin())
k = int(fastin())
d = [[0] * (k+1) for _ in range(n+1)]
if n / k < 2 : 
  print(0)
  sys.exit()
if k == 1 : 
  print(n)
  sys.exit()
for i in range(1,n+1):
  d[i][1] = i
for i in range(4,n+1):
  for j in range(2, k+1):
    d[i][j] =  d[i-1][j] + d[i-2][j-1]

print(d[n][k] % 1000000003)