'''
import sys
input = sys.stdin.readline

n = int(input())
result = []
cnt = 0
def hanoi(num,a,b,c):
  if num == 1:
    result.append([a,b])
    global cnt
    cnt += 1
  else:
    hanoi(num-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(num-1,c,b,a)

hanoi(n,1,3,2)
print(cnt)
for i in range(len(result)):
  print(result[i][0],end=" ")
  print(result[i][1])
'''
'''
import sys
input = sys.stdin.readline

n = int(input())
result = []

def hanoi(num,a,b,c):
  if num == 1:
    result.append([a,b])
  else:
    hanoi(num-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(num-1,c,b,a)
res = 0
for _ in range(n):
  res = 2 * res + 1 
hanoi(n,1,3,2)
print(res)
for i in range(len(result)):
  print(result[i][0],end=" ")
  print(result[i][1])   
'''

import sys
input = sys.stdin.readline

n = int(input())

def hanoi(num,a,b,c):
  if num == 1:
    print(a,b)
  else:
    hanoi(num-1,a,c,b)
    hanoi(1,a,b,c)
    hanoi(num-1,c,b,a)
result = 0
for _ in range(n):
  result = 2 * result + 1
print(result) 
hanoi(n,1,3,2)