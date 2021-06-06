import heapq
def solution(jobs):
    n = len(jobs)
    t1 = 0
    t2 = -1
    answer = 0
    q = []
    cnt = 0
    
    while cnt<n:
        for i in jobs:
            if t2<i[0]<=t1:
                heapq.heappush(q, [i[1], i[0]])
        if q:
            now = heapq.heappop(q)
            t2 = t1
            t1 += now[0]
            answer += t1 - now[1]
            cnt += 1
        else: t1 += 1
    
    return int(answer/n)