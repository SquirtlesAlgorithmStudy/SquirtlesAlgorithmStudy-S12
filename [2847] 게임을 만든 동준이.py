## 2847 게임을 만든 동준이
level = int(input())

# s=받아온 점수
s=list(range(level))
for i in range(level):
  s[i]=int(input())

# n=빼야하는 점수
n=list(range(level))

for j in range(level):
  i=(j+1)*(-1)
  if i==-1:
    n[i]=0
  else:
    if s[i]>s[i+1]:
      n[i]=s[i]-s[i+1]+1
      s[i]=int(s[i])-int(n[i])
    elif s[i]==s[i+1]:
      n[i]=1
      s[i]=int(s[i]-1)
    else:
      n[i]=0

total=sum(n)
print(total)