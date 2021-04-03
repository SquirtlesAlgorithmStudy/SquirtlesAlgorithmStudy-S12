import sys
fastin = sys.stdin.readline
n = int(fastin())
price = []
price.append(0)
price += list(map(int,fastin().split()))

d = [0] * (n+1)
d[1] = price[1]
for i in range(2, n+1):
  d[i] = price[i]
  for j in range(1, (i // 2)+1):
    d[i] = max(d[i], d[i-j]+d[j])
print(d[n])