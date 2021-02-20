import sys
cin = sys.stdin.readline

#배열 출력
n = int(cin())
pingping = [[0] * n for _ in range(n)] #n*n 배열 생성


now = (n//2,n//2) #초기좌표 (정중앙)
dx = [-1,0,1,0]
dy = [0,1,0,-1]  #상/우/하/좌
i =1

step=1
pingping[now[0]][now[1]] = i #정가운데에 1 저장하면서 시작.
i+=1  #i를 1증가시킴


while(i<n*n): #n*n이 될때 까지만 반복
    for up in range(step):
      if i>n*n: break #n*n이 되면 for문 탈출
      now = (now[0]+dx[0],now[1]+dy[0]) #현재좌표를 한칸 위로 이동
      pingping[now[0]][now[1]] = i #현재 위치에 i 저장
      i+=1 #i를 1 증가시킴
    
    for right in range(step):
      if i>n*n: break
      now = (now[0]+dx[1],now[1]+dy[1])
      pingping[now[0]][now[1]] = i
      i+=1
    step+=1

    for down in range(step):
      if i>n*n: break
      now = (now[0]+dx[2],now[1]+dy[2])
      pingping[now[0]][now[1]] = i
      i+=1
    for left in range(step):
      if i>n*n: break
      now = (now[0]+dx[3],now[1]+dy[3])
      pingping[now[0]][now[1]] = i
      i+=1
    step+=1

#전체 배열 출력
for i in range(n):
  for j in range(n):
    print(pingping[i][j],end=' ')
  print('')



#입력받은 숫자의 좌표
x = int(cin())

for i in range(n):
  for j in range(n):
    if pingping[i][j] == x: print(i+1,j+1)
  