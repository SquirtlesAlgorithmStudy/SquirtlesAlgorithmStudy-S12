import sys
cin = sys.stdin.readline

n, k = cin().split()
n = int(n)
k = int(k)
table = list(cin().rstrip())
cnt = 0;

for i in range(n):
  if table[i] == 'P':
    for j in range(-k,k+1): #P주변 k범위 안에서
      if i+j < 0 or i+j >= n : continue #index범위를 넘어 갈경우 예외처리
      if table[i+j] == 'H': #왼쪽부터 H탐색
        table[i+j] = 'O' #'O'는 먹었음을 의미
        cnt+=1 #햄버거 먹은 사람 카운트
        break #1인당 1햄버거만 먹으므로 반복문 탈출

print(cnt)