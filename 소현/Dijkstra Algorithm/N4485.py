# 작성자 : SH_WON_96
# 2021-04-16    
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : 4485 녹색 옷 입은 애가 젤다지?

# [0][0] 에서 [N-1][N-1] 까지 이동하면서 최소 합 구하기
# 초기 입력값 받기
import sys
import heapq
fast_in = sys.stdin.readline

def test(N):
    matrix = []
    weight = [[float("INF")]*N for _ in range(N)]
    for _ in range(N):
        matrix.append(list(map(int,fast_in().strip().split())))

    weight[0][0] = matrix[0][0]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    heap = []
    heapq.heappush(heap,(weight[0][0],0,0))

    while heap:
        w, x, y = heapq.heappop(heap)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if w + matrix[nx][ny] < weight[nx][ny]:
                    weight[nx][ny] = w + matrix[nx][ny]
                    heapq.heappush(heap,(weight[nx][ny],nx,ny))

    return weight[N-1][N-1]



i = 1
while True:
    N = int(fast_in().strip())
    if N == 0 :
        break
    result = test(N)
    print("Problem " + str(i) + ": " + str(result))
    i += 1