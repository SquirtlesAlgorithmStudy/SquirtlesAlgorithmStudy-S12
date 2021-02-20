import sys
cin = sys.stdin.readline

n = int(cin().rstrip())
score = []
cnt=0

for i in range(n):
  score.append(int(cin()))

#score = [int(cin()) for _ in range(n)]

for i in range(n-1,0,-1):
  while score[i] <= score[i-1]:
    score[i-1]-=1
    cnt+=1

print(cnt)