import sys
input = sys.stdin.readline
from collections import deque


# n, k 입력
n = int(input())
k = int(input())


# 사과 생성
apple = []
for _ in range(k):
  i, j = map(int,input().split())
  apple.append([i-1,j-1])

# 방향 전환 정보 생성
l = int(input())
moves = dict()
for _ in range(l):
  move, direct_chan = input().split()
  moves[int(move)] = direct_chan

# 뱀, 시간 초기화
snake = deque()
direction = 0
t = 0
snake.append([0,0])
head_pos = [0,0]

# 방향 전환 함수
def directionChanger(a):
  global direction 
  if a == 'L':
    direction += 1
    if direction == 4 : direction = 0
  else:
    direction -= 1
    if direction == -1 : direction = 3
  
# 이동 시작  
while True:
  t += 1
  if (t-1) in moves: directionChanger(moves[t-1])
  if direction == 0:
    if (head_pos[1] + 1) == n:
      print(t)
      break  
    head_pos[1] += 1
    if head_pos in snake:
      print(t)
      break
    snake.append([head_pos[0],head_pos[1]])
    if head_pos in apple:
      apple.remove(head_pos)
    else:snake.popleft()
      
    

  elif direction == 1:
    if (head_pos[0] - 1) == -1:
      print(t)
      break
    head_pos[0] -= 1
    if head_pos in snake:
      print(t)
      break
    snake.append([head_pos[0],head_pos[1]])
    if head_pos in apple:
      apple.remove(head_pos)
    else:snake.popleft()

  elif direction == 2:
    if (head_pos[1] - 1) == -1:
      print(t)
      break
    head_pos[1] -= 1
    if head_pos in snake:
      print(t)
      break
    snake.append([head_pos[0],head_pos[1]])
    if head_pos in apple:
      apple.remove(head_pos)
    else:snake.popleft()

  else:
    if (head_pos[0] + 1) == n:
      print(t)
      break
    head_pos[0] += 1
    if head_pos in snake:
      print(t)
      break
    snake.append([head_pos[0],head_pos[1]])
    if head_pos in apple:
      apple.remove(head_pos)
    else:snake.popleft()       