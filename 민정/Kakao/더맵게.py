import sys
# import heapq
# sys.setrecursionlimit(10 ** 9)

def solution(scoville, K):
  answer = 0

  heap = []
  for i in scoville:
    heapq.heappush(heap, i)

  while heap[0]<K:

    if len(heap) <= 1:
      answer = -1
      break

    first = heapq.heappop(heap)
    second = heapq.heappop(heap)

    new = first + (2*second)

    heapq.heappush(heap, new)
    answer += 1
  return answer