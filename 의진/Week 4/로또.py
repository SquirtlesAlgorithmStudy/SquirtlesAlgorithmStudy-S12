import sys
input = sys.stdin.readline
from itertools import combinations

data = []
i = 0
while True:
  data.append(list(map(int,input().rstrip().split())))
  if data[i][0] == 0 : break
  i += 1
result = []

for j in range(i):
  comb = list(combinations(range(1,data[j][0]+1),data[j][0]-6))
  for k in sorted(comb, reverse = True):
    kl = list(k)
    kl.reverse()
    result = data[j][1:]
    for l in kl:
      del result[l-1]
    for m in range(len(result)):
      print(result[m], end=" ")
    print("")
  print("")

'''
from itertools import *
while True:
    n = input().split()[1:]
    if not n:
        break
    for c in combinations(n,6):
        print(" ".join(c))
    print()
'''
    
    




