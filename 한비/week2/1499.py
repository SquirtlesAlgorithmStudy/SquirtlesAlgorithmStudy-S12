import sys
input=sys.stdin.readline

N,k=map(int, input().split()) #N:물새는곳개수/k:테이프길이
li=list(map(int, input().split()))
li.sort()

s=li[0]
a=1

for i in range(1, len(li)):
    if li[i] < s+k:
        continue
    else:
        a=a+1
        s=li[i]
        
            
print(a)