import sys
fastin = sys.stdin.readline

d, k = map(int,fastin().split())
d-=1

pibo = [1, 1]
for i in range(d-2):
  pibo.append(pibo[i+1] + pibo[i])

for b in range(1, (k // pibo[d-1]) + 1):
  r = k - pibo[d-1] * b
  a = r // pibo[d-2]
  if(r % pibo[d-2] == 0 and a <= b):
    print(a)
    print(b)
    break