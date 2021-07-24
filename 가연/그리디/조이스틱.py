alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_r='NOPQRSTUVWXYZ'

name=input()
for i in range(int(len(name))):
  #A~Z 문자열에서 주소 찾기
  num=alpha.find(name[i])
  #주소가 A~M 사이라면 그대로 쓰고,
  #N~Z 사이라면 원래 주소 -0 -2 -4 -6 ...
  if num < 12:
    print(alpha.find(name[i]))
  else:
    print(num-(alpha_r.find(name[i])*2))
  
#조이스틱 왼쪽은 모르겠다...