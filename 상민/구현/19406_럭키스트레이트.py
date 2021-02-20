import sys

cin = sys.stdin.readline

score = list(map(int,cin().rstrip()))
mid = len(score)//2
lsum =0
rsum =0

for i in range(mid):
  lsum+=score[i]
for i in range(mid,len(score)):
  rsum+=score[i]

if lsum==rsum: print("LUCKY")
else : print("READY")
