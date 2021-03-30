import sys  
fastin = sys.stdin.readline
n = int(fastin())
tri = []
for _ in range(n):tri.append(list(map(int,fastin().split())))
d = []
for i in range(n):
  temp = []
  for j in range(i+1):
    temp.append(0)
  d.append(temp)  
for i in range(n):
  for j in range(i+1):
   if j == 0 : d[i][0] = d[i-1][0] + tri[i][0]
   elif j == i : d[i][i] = d[i-1][i-1] + tri[i][i]
   else: d[i][j] = max(d[i-1][j-1], d[i-1][j]) + tri[i][j]

print(max(d[n-1][:]))




