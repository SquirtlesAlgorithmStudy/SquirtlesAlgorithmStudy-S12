import sys
input=sys.stdin.readline

n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
ans=0

for _ in range(n):
    x,y=map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time=t[i]+i
    if time <= n:
        dp[i]=max(p[i]+dp[time], ans)
        ans=dp[i]
    else:
        dp[i]=ans

print(ans)