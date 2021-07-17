## 1439 뒤집기
s=input()
len_s=len(s)

c_0=s.count('0')
c_1=s.count('1')
n=0
t=0

if (c_0 < c_1):
  n=c_0
  for i in range(len_s): 
    if s[i-1]=='0' and s[i-1]==s[i]:
      t=t+1
else:
  n=c_1
  for i in range(len_s): 
    if s[i-1]=='1' and s[i-1]==s[i]:
      t=t+1

num=n-t
print(num)