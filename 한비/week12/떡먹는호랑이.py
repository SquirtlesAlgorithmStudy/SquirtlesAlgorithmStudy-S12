import sys

input=sys.stdin.readline()


d,k = map(int,input().split())

dp = [ [0,0] for _ in range(d)] 

dp[0] = [1,0] #첫째날
dp[1] = [0,1] #둘째날

for i in range(2,d):
  dp[i][0] = dp[i-2][0] + dp[i-1][0] 
  dp[i][1] = dp[i-2][1] + dp[i-1][1]

for i in range(1, k//2+1):
  a=k-dp[d-1][0]*i
  if  a % dp[d-1][1] == 0 : #첫번째날 떡의 개수가 두번째날 떡의 개수와 나눠떨어지면
    print(i)
    print((k - dp[d-1][0]*i) // dp[d-1][1])
    break