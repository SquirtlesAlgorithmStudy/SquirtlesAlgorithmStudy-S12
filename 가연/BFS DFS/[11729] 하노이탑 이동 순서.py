##[11729] 하노이탑 이동 순서

n = int(input())

#n: 원반수, s:시작원반, e: 끝원반, a:보조원반
def hanoi(n,s,e,a):
  if n==1:
    print(s,e)
    return
    
  hanoi(n-1,s,a,e)
  print(s,e)
  hanoi(n-1,a,e,s)
  
print(2**n-1)
hanoi(n,1,3,2)