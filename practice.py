#1913 달팽이
n=int(input())
li= [[0]*n for i in range(n)]
k=0

for i in range(n):
  for j in range(n):
    k=k+1
    li[i][j]=k
    print(li[i][j],end=" ")
  print("\n")

#기준점
p=(n-1)/2

li[p][p]=1
li[p-1][p]=2
li[p-1][p+1]=3
li[p][p+1]=4
li[p+1][p+1]=5
li[p+1][p]=6
li[p+1][p-1]=7
li[p][p-1]=8
li[p-1][p-1]=9
li[p-2][p-1]=10
print(li)