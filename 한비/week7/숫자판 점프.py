import sys
input=sys.stdin.readline

matrix=[]
for i in range(5):
  matrix.append(list(map(str, input().split()))) #str로 받아야 문자열로 이어짐

def dfs(x,y,number):
  if len(number)==6:
    if number not in answer:
      answer.append(number)
    return

  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or nx>=5 or ny<0 or ny>=5:
      continue
    else:
      dfs(nx,ny,number+matrix[nx][ny])

answer=[]
for i in range(5):
  for j in range(5):
    dfs(i,j, matrix[i][j])
print(len(answer))