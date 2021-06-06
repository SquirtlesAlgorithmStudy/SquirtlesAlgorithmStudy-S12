import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
k = int(input())
# n개중 k개를 고르는 방법을 기록하기 위한 list
ans = [[0]*(n+1) for _ in range(n+1)]

def pick(n, k, a):
  # n개의 절반을 고르는 방법은 당연히 2가지 (n%2=0일때)
  if (n/k==2): return 2 
  # n개 중 하나를 고르는 방법은 n가지
  if (k==1): return n
  # n개중 k 고르는 방법이 기록이 안되어있으면
  if (a[n][k]) == 0:
    # 재귀
    ans = pick(n-1,k,a)+pick(n-2,k-1,a)
    a[n][k] = ans
  return a[n][k]

if (n/2 < k): print(0)
else: print(pick(n,k,ans)%1000000003)