import sys
from math import inf

input=sys.stdin.readline
n = int(input()) #도시 수
m = int(input()) #버스 수

cost = [[inf] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c) #입력 값부터 최소로 업데이트

# 플로이드 와샬 알고리즘 적용
for k in range(n): #경유지
    cost[k][k] = 0
    for i in range(n): #출발점
        for j in range(n): #도착점
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

# 결과 출력
for r in cost:
    for i in range(n):
        if r[i] == inf:
            r[i] = 0 #갈수없으면, 0 출력
        print(r[i], end=" ")
    print()