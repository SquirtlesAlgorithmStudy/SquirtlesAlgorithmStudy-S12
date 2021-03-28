n=int(input())
p=[tuple(map(int,input().split()))for _ in range(n)]
d=[0]*(n+1);i=1
while i<=n:
 for j in range(i):
  if i-j>=p[j][0]:d[i]=max(d[i],d[j]+p[j][1]) 
 i+=1
print(d[i-1]) 