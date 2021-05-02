import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def pick(n, k, a):
  if (n/k==2): return 2
  if (k==1): return n
  if (a[n][k]) == 0:
    ans = pick(n-1,k,a)+pick(n-2,k-1,a)
    a[n][k] = ans
  return a[n][k]

n = int(input())
k = int(input())
ans = [[0]*(n+1) for _ in range(n+1)]

if (n/2 < k): print(0)
else: print(pick(n,k,ans)%1000000003)