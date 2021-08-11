def solution(name):
  alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  alpha_r='NOPQRSTUVWXYZ'

  result=[]

  ## 정주행 ###############################
  n1=0
  a1=0

  for i in range(int(len(name))):
    #A~Z 문자열에서 주소 찾기
    num=alpha.find(name[i])
   #주소가 A~M 사이라면 그대로 쓰고,
    #N~Z 사이라면 원래 주소 -0 -2 -4 -6 ...
    if num < 12:
      up=alpha.find(name[i])
      a1+=up
    else:
      down=num-(alpha_r.find(name[i])*2)
      a1+=down
    n1+=1

  for i in range(len(name)):
    #맨 뒤의 연속된 A개수만큼을 탐색 수에서 뺀다.
    temp=len(name)-i
    if name[i:len(name)]=='A'*temp:
      n1=n1-temp
      break

  a1+=n1-1
  ##print(a1)

  ## 역주행 #############################
  n2=0
  a2=0

  for i in range(1,int(len(name))+1):
    num=alpha.find(name[-i])

    if num < 12:
      up=alpha.find(name[-i])
      a2+=up
    else:
      down=num-(alpha_r.find(name[-i])*2)
      a2+=down
    n2+=1

  for i in range(1,len(name)+1):
    #맨 앞의 연속된 A개수
    temp=len(name)-(i-1)

    if name[-len(name):-i+1]=='A'*temp:
      n2=n2-temp
      break

  a2+=n2
  ##print(a2)

  ##찍고 턴하기 ############################
  n3=0
  n3_back=0
  na=0
  an=0
  a3=0
  list=[]

  for i in range(int(len(name))):
    num=alpha.find(name[i])

    if num < 12:
      up=alpha.find(name[i])
      a3+=up
    else:
      down=num-(alpha_r.find(name[i])*2)
      a3+=down
    n3+=1

  for i in range(1,len(name)):
    #연속된 A개수 > A앞의 숫자 개수일 경우 찍고턴
    #맨 뒤의 연속된 A개수만큼을 탐색 수에서 뺀다.
    #BAAABBBBBBB
    half=int(len(name)/2)

    if name[i-1:i+1] == 'A'*2:
      list.append(i-1)
      list.append(i)
      print(list)

      na=int(list[0]) #A묶음 시작점
      an=int(list[-1]) #A묶음 끝나는 점
      #연속된 A묶음 앞의 숫자 개수 : name[0:na]
      #연속된 A묶음 : name[na:an+1]
      #BAAABBBBBBB
   
  if name[i-1:i+1] == 'A'*2 and len(name[0:na]) <= len(name[na:an+1]):
    print('success')
    if list[0]==0:
      n3=len(name)-list[-1]-1
    else:
      n3=(list[0]-1)*2 + len(name)-(list[-1]+1)
      n3_back=list[0]-1 + 2*(len(name)-list[-1]-1)

    if n3<=n3_back:
      a3+=n3
    else:
      a3+=n3_back
    result.append(a3)
    print(a3)

  elif len(name)==3 and name[1]=='A':
    n3=1
    a3+=n3
    result.append(a3)
    print(a3)

    #A묶음 앞까지 이동횟수*2 + A묶음 뒤 역주행횟수
    #A묶음 앞까지 이동횟수: A시작점 주소 : list[0]
    #A묶음 뒤 역주행 횟수: name길이-list[마지막]-1

## a1, a2, a3 중 가장 작은 값 출력

  result.append(a1)
  result.append(a2)

  answer=min(result)
  return answer

print(solution('ZAAAZZZZZZZ'))