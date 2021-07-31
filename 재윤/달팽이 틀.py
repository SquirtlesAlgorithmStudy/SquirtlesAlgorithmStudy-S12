N = int(input())
k = int(input())

A = N//2

board = [[0]*N for _ in range(N)] 
'''
위로갈때 dx,dy =0, -1  > u
오른쪽   dx,dy = 1,0   > r
아래로    dx,dy = 0,1  > d
왼쪽     dx,dy = -1, 0 > l


if N = 3 :
  u,d,l,r,u = 1, 1, 2, 2, 2
if N = 5 :
  u,d,l,r,u = 1, 3, 4, 4, 4
if N = 7 :
  u,d,l,r,u = 1, 5, 6, 6, 6
if N = K:
  u,d,l,r,u = 1, k-2, k-1, k-1, k-1 <<<규칙
  n = 3 > 1바퀴 3
  n = 5 > 2바퀴 3 5
  n = 7 > 3바퀴 3 5 7
'''
dy = [0,1,0,-1]
dx = [-1,0,1,0]

# x, y 는 시작행렬
x,y = (N//2,N//2)
index = 1
board[x][y] = 1

for i in range(1,A+1):
    for _ in range(1): # up
        x = x + dx[0]
        y = y + dy[0]
        index += 1
        board[x][y] = index
        
    for _ in range(2*i-1): # right
        x = x + dx[1]
        y = y + dy[1]
        index += 1
        board[x][y] = index
        
    for _ in range(2*i): # down
        x = x + dx[2]
        y = y + dy[2]
        index += 1
        board[x][y] = index
    for _ in range(2*i): # left
        x = x + dx[3]
        y = y + dy[3]
        index += 1
        board[x][y] = index
    for _ in range(2*i): # up
        x = x + dx[0]
        y = y + dy[0]
        index += 1
        board[x][y] = index
        
for x in range(N):
    for y in range(N):
        print(board[x][y], end= " ")
    print("")

for x in range(N):
    for y in range(N):
        if board[x][y] == k : print(x+1, y+1)
            
