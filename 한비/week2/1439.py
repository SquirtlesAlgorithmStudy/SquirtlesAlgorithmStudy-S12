
#import sys 
for _ in range(int(input())):
    li = list(map(int, input().split()))
#sys.stdin.readline()
ans = 0
for i in range(len(li)-1):
    if li[i] <= li[i+1]:
        m = li[i+1] - li[i] + 1
        ans += m
        li[i+1] -= m 
print(ans)


print(li)