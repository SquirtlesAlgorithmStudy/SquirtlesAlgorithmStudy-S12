import sys
import math
cin = sys.stdin.readline

cnt=0
s = list(map(int,cin().rstrip()))

for i in range(len(s)-1):
  if s[i] != s[i+1]: cnt+=1

print(math.ceil(cnt/2)) #round(cnt/2)를 하면 오류가 난다.