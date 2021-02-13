import sys
input=sys.stdin.readline

N,k=map(int, input().split())
s=list(input().strip())

a=0

for i in range(len(s)):
    if(s[i]=='P'):
        if i<k:
            for j in range(0, i+k):
                if s[j]=='H':
                    s[j]=='E'
                    a=a+1
                    break
        else:
            for j in range(i-k, i+k+1):
                if s[j]=='H':
                    s[j]=='E'
                    a=a+1
                    break
print(a)