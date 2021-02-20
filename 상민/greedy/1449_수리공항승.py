import sys
cin = sys.stdin.readline
n, l = cin().split()
n = int(n)
l = int(l)
water = list(map(int,cin().split()))

water.sort()
cover = water[0]+l-.5
cnt = 1

for i in range(n):
  if water[i] <= cover:
    continue
  cover = water[i] + l-.5
  cnt+=1

print(cnt)