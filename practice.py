#햄버거 분배
n,k =map(int, input().split())
p=input()
list_p=list(p)
hp=0

for i in range(n):
  if (p[i]=='P'):
    if (k==1):
      for j in range(k):
        if (p[i-k-j]=='H'):
          list_p[i-k-j]='X'
        elif (p[i+k+j]=='H'):
          list_p[i+k+j]='X'
    else:
      for j in range(k):
        if (p[i-k-j+1]=='H'):
          list_p[i-k-j+1]='X'
        elif (p[i+k+j-1]=='H'):
          list_p[i+k+j-1]='X'

    
np=''.join(list_p)
hp=np.count('X')
print(hp)