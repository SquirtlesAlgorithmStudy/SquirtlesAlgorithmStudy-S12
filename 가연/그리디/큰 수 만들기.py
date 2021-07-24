#큰 수 만들기
number=input()
k=int(input())
m=max(number)
m_address=number.find(m)

if len(number[m_address+1:])>=len(number)-k-1:
  m2=max(number[m_address+1:])
  print(m2)

print(int(m+m2))