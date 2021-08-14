from collections import deque
import sys
fastin = sys.stdin.readline
n, m = map(int, fastin().split())
board = []
for _ in range(n):
  board.append(list(fastin().strip()))

r = [(i,j) for i in range(n) for j in range(m) if board[i][j]=='R'] 
b = [(i,j) for i in range(n) for j in range(m) if board[i][j]=='B']

rx, ry = r[0]
bx, by = b[0]


def bfs(rx, ry, bx, by, board):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((rx, ry, bx, by, 1))
  visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
  visited[rx][ry][bx][by]= 1
  
  
  is_game_over = 0
  is_red_clear = 0

  while queue:
    rx, ry, bx, by, depth = queue.popleft()
    if depth > 10 : break
    #print(rx, ry)
    for i in range(4):
      x_finish = 0; y_finish = 0
      a = 1
      
      while True:
        if a : crx = rx; cry = ry; cbx = bx; cby = by ; a = 0
        else : crx = nrx; cry = nry; cbx = nbx; cby = nby
        if (board[crx+dx[i]][cry+dy[i]] != '#' )and (not ((cbx == crx + dx[i]) and(cby == cry + dy[i]))) and (is_red_clear == 0):
          nrx = crx + dx[i]
          nry = cry + dy[i]
         
        elif is_red_clear : nrx = 0; nry = 0; x_finish = 1
        else : nrx = crx; nry = cry; x_finish = 1

        if (board[cbx+dx[i]][cby+dy[i]] != '#') and not ((nrx == cbx + dx[i]) and(nry == cby + dy[i])):
          nbx = cbx + dx[i]
          nby = cby + dy[i]
        
        else : nbx = cbx; nby = cby; y_finish = 1

        if board[nbx][nby] == 'O' : 
          is_game_over = 1
          break 
        if board[nrx][nry] == 'O' : 
          is_red_clear = 1

        if x_finish and y_finish : break
      if is_game_over : 
        is_game_over = 0
        is_red_clear = 0
        continue
      if is_red_clear and y_finish:
        return depth

      
      if (visited[nrx][nry][nbx][nby] == 0):
        visited[nrx][nry][nbx][nby] = 1
        #print('append', nrx, nry)
        queue.append((nrx, nry, nbx, nby, depth +1))
        
  return -1  
        

print(bfs(rx, ry, bx, by, board))      
  
