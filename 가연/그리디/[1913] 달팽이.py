#[1913] 달팽이

N=int(input())
num_f=int(input())
answer=[]

matrix=[[0]*N for i in range(N)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

mid=int((N-1)/2) #기준점
matrix[mid][mid]=1

x=0
y=0
num=2

for i in range(N*2):
  if i%2==0:
    j=int(i/2)+1
    
  for k in range(j):
    x=x+int(dx[i%4])
    y=y+int(dy[i%4])

    if mid+x<0 or mid+y<0:
      break
    
    matrix[mid+x][mid+y]=num
    
    if num_f==1:
      answer.append(mid+1)
      answer.append(mid+1)
    elif matrix[mid+x][mid+y]==num_f:
      answer.append(mid+x+1)
      answer.append(mid+y+1)
    num=num+1

#수정된 리스트 출력
for i in matrix:
  for j in i:
    print(j, end=' ')
  print()

print(answer[0], answer[1])
