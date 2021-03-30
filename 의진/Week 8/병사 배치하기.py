import sys 
fastin  = sys.stdin.readline

n = int(fastin().strip())
sol = list(map(int, fastin().strip().split()))
sol.reverse()

d = [1]*n

for i in range(1,n):
  for j in range(i):
    if sol[j] < sol[i]: d[i] = max(d[i],d[j]+1)
print(n-max(d))


