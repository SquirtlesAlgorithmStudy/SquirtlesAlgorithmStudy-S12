N = int(input())
li = [int(input()) for _ in range(N)]

a=0

for i in range(N-1, 0, -1): #앞에서 검사하면 복잡, 뒤에서부터올것
    if li[i]<=li[i-1]:
        a=a+(li[i-1]-li[i]+1)
        li[i-1]=li[i]-1
        
print(a)