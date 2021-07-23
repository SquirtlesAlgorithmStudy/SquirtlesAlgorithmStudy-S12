N = int(input())
num = int(input())

for i in range(N):
    board = [0] * N
    board.append(N) 
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
'''
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# x, y 는 시작행렬
x,y = (N//2,N//2)
i =1
board[x][y] = i
i += 1
for i in range(N//2):
    for up in range(1):
        x = x + dx[0]
        y = y + dy[0]
        board[x][y] += 1
    for right in range(N-2):
        x = x + dx[1]
        y = y + dy[1]
        board[x][y] += 1
    for down in range(N-1):
        x = x + dx[2]
        y = y + dy[2]
        board[x][y] += 1
    for left in range(N-1):
        x = x + dx[3]
        y = y + dy[3]
        board[x][y] += 1
    for up in range(N-1):
        x = x + dx[0]
        y = y + dy[0]
        board[x][y] += 1
