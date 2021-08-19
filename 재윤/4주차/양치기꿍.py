'''
전체 좌표에서 v,k를 찾아낸다음 #이 있을때까지 bfs 돌림
v,k를 추가로 발견하면 +=1
만약 v > s  = s는 0 ( 다 잡아먹힘)
     s > v  = v는 0 ( 다 잡아먹힘)


으아아아아 왜 안되는데 왜오 ㅗ애ㅗ애애ㅗ애
'''


# R, C 받아옴
R,C = map(int, input().split())

# 리스트 만들고 wolf, sheep = 0 , 입력값 받아옴
board = []
wolf = 0
sheep = 0
for _ in range(R):
    board.append(list(input().rstrip()))



def bfs(x,y):
    if board[x][y] != '#' and 0<= x <= C and 0 <= y <= R :
        if board[x][y] == 'v' :
            wolf += 1
            board[x][y] == 'P'
        elif board[x][y] == 'k' :
            sheep += 1
            board[x][y] == 'P'
        bfs(x-1,y)
        bfs(x,y-1)
        bfs(x+1,y)
        bfs(x,y+1)
    return True

for x in range(C):
    for y in range(R):
        if board[x][y] == 'k' or 'v' :
            bfs(x,y)
            if wolf > sheep :
                sheep = 0
            else :
                wolf = 0

print(sheep, wolf, end=" ")
