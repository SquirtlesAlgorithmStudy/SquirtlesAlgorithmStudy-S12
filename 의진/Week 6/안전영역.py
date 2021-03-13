import sys 
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input().strip())
board = [list(map(int,input().strip().split())) for _ in range(n)]

def dfs(x,y,k):
  
  if 0 <= x < n and 0 <= y < n :
    
    if (board[x][y] >= k) and (visited[x][y] == 0):
      visited[x][y] = 1
      dfs(x-1, y, k)
      dfs(x, y-1, k)
      dfs(x+1, y, k)
      dfs(x, y+1, k)
      return True
  return False

result = []

m = max(max(board))


for i in range(1, m+1):
  visited = [[0]*n for _ in range(n)]
  cnt = 0
  for j in range(n):
    for k in range(n):
      if dfs(j, k, i) == True:
        cnt+=1
  result.append(cnt)
print(max(result))  

