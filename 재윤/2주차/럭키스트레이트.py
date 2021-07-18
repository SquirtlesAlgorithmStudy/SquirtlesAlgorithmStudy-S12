import sys

N = sys.stdin.readline().rstrip()

left = 0
right = 0

while len(N) % 2 != 0:
    print("다시 입력해주세요")
    N = sys.stdin.readline().rstrip()
    
for i in range(len(N)//2):
  num = int(N[i])
  left += num
 
for i in range(len(N)//2, len(N)):
  num = int(N[i]) 
  right += num
 
if left == right:
  print("LUCKY")
else:
  print("READY") 
