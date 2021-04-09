# 작성자 : SH_WON_96
# 2021-04-09
# 알고리즘 - Floyd Warshall Algorithm
# 문제번호 : 11404 플로이드

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

n = int(fast_in().strip())
m = int(fast_in().strip())
matrix = [[float("inf")]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y, w = map(int,fast_in().strip().split())
    if w < matrix[x][y]:
        matrix[x][y] = w

for i in range(1,n+1):
    matrix[i][i] = 0

for k in range(1,n+1):
    # k를 경유해서 갈 때
    for i in range(1,n+1):
        for j in range(1,n+1):
            # i에서 j로 바로 가는 것이랑 k 경유해서 가는것이랑 비교하기
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if matrix[i][j] != float("inf"):
            print(matrix[i][j], end= " ")
        else:
            print(0, end=" ")
    print()

