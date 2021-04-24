import sys
import collections
import heapq

INF = float('inf')
input = sys.stdin.readline
n, e = map(int, input().split())
g = collections.defaultdict(list)

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

v1, v2 = map(int, input().split())
    
def dijkstra(s):
    dist = [INF] * (n+1)
    dist[s] = 0
    q = [[dist[s], s]]
    while q:
        u = heapq.heappop(q)[1]
        for v, c in g[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heapq.heappush(q, [dist[v], v])
    return dist

def solve():
    from_1 = dijkstra(1)
    from_v1 = dijkstra(v1)
    from_v2 = dijkstra(v2)

    path1 = from_1[v1] + from_v1[v2] + from_v2[n]
    path2 = from_1[v2] + from_v2[v1] + from_v1[n]

    result = min(path1, path2)
    
    if result < INF:
        return result
    else:
        return -1

print(solve())