# 작성자 : SH_WON_96
# 2021-04-09
# 알고리즘 - Floyd Warshall Algorithm
# 문제번호 : 11403 경로 찾기

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())

matrix = []
for i in range(N):
    tmp = list(map(int,fast_in().strip().split()))
    matrix.append(tmp)

for k in range(N):
    # k를 경유해서 갈 때
    for i in range(N):
        for j in range(N):
            # i에서 j로 바로 가는 것이 존재하면 그냥 냅두면 되고, 없으면 k를 경유해서 가는 것을 넣어주면 되니깐
            if matrix[i][k] ==1 and  matrix[k][j] == 1:
                matrix[i][j] = 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            print(1, end= " ")
        else:
            print(0, end = " ")

    print()