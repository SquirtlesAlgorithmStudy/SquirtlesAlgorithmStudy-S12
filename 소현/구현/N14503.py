# 작성자 : SH_WON_96
# 2021-03-17
# 알고리즘 - 구현
# 문제번호 : 14503
fast_in = sys.stdin.readline

N, M = map(int, fast_in().strip().split())
r,c,d = map(int, fast_in().strip().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, fast_in().strip().split())))

dx = [-1,0,1,0] # 북,동,남,서
dy = [0,1,0,-1]


queue = deque([])
queue.append((r,c))
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1

def bfs(matrix,q,d):
    count = 1 # 청소한 칸 수
    while q:
        x,y = q.popleft()
        change = False
        check = 0
        for i in range(1,5):
            nx = x + dx[(d-i)%4] # d의 왼쪽방향부터 시작
            ny = y + dy[(d-i)%4]
            check += 1
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 0 and visited[nx][ny] == 0: # 미방문에 빈칸
                    d = d - i
                    visited[nx][ny] = 1
                    count += 1
                    change = True
                    q.append((nx,ny))

            if change:
                break
            if check == 4: # 4방향 모두 체크
                nx = x-dx[(d-i)%4]
                ny = y-dy[(d-i)%4]
                if matrix[nx][ny] == 0: #후진 가능하면 후진 하기
                    q.append((nx,ny))

    return count

print(bfs(matrix,queue,d))