# 작성자 : SH_WON_96
# 2021-02-19
# 알고리즘 - 구현
# 문제번호 : 1913 달팽이

# 초기 입력값 받기
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

# N*N 만들기
matrix = [[0]*(N) for i in range(N)]

center = (N//2)

x = N//2
y = N//2

matrix[x][y] = 1
i = 2

di = [-1,0,1,0]
dj = [0,1,0,-1]
where = []

breaker = False
for n in range(1,N+1):
    if n%2 == 1:
        for t in range(2):
            for k in range(n):
                x = x + di[t]
                y = y + dj[t]
                matrix[x][y] = i
                if i == M:
                    where.append((x+1,y+1))
                i += 1
                if i > N**2:
                    breaker = True
                    break
            if breaker:
                break
    else:
        for t in range(2,4):
            for k in range(n):
                x = x + di[t]
                y = y + dj[t]
                matrix[x][y] = i
                if i == M:
                    where.append((x+1,y+1))
                i += 1
                if i > N**2:
                    breaker =  True
                    break
            if breaker:
                break

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end = " ")
    print()

print(where[0][0],where[0][1])

