# 작성자 : SH_WON_96
# 2021-04-23
# 알고리즘 - Dijkstra Algorithm
# 문제번호 : https://programmers.co.kr/learn/courses/30/lessons/12978

import heapq
def solution(N, road, K):

    matrix = [[float("INF")] * (N + 1) for _ in range(N + 1)]
    time = [float("INF")] * (N + 1)
    connection = [[] for _ in range(N + 1)]
    for f, t, w in road:
        if w < matrix[f][t]:
            matrix[f][t] = w
            matrix[t][f] = w
            connection[f].append(t)
            connection[t].append(f)

    time[1] = 0
    heap = []
    for t in connection[1]:
        w = matrix[1][t]
        if w <= K:
            time[t] = w
            heapq.heappush(heap, (w, t))

    while heap:
        w, v = heapq.heappop(heap)
        for t in connection[v]:
            wei = matrix[v][t]
            if w + wei <= K and w + wei < time[t]:
                time[t] = w + wei
                heapq.heappush(heap, (w + wei, t))

    print(time)
    count = 0
    for tmp in time:
        if tmp != float("INF"):
            count += 1
    return count

