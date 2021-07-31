#큰 수 만들기
def solution(number, k):
  #가장 큰 수를 기준점으로
  m=max(number[:-k])
  m_ad=number.find(m)
  ml=[m]
  answer=''
  print(m_ad)

  for i in range(len(number)-k-1):
    print(number[m_ad+i+1:len(number)-k+i+1])
    #print('시작: ', m_ad+i)
    #print('끝: ', number[-k+i])
    ml.append(max(number[m_ad+i+1:len(number)-k+i+1]))

  #i번째 기준점 ~ number[:-k+i]에서 기준점 number-k개 만들기 & 리스트
  #기준점 리스트 요소 전부 더하기

  print(ml)

  for i in range(len(number)-k):
    answer+=ml[i]
  return answer
  
print(solution('1924',2))
