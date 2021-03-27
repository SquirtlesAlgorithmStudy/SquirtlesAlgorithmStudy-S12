n = int(input())
arr = list(map(int,input().split()))
arr.reverse()

# 1 로 초기화 하는 이유는 적어도 자기 자신은 존재하기 때문.
dp = [1] * n

for i in range(1,n):
# dp[i] = i 를 마지막 원소로 가지는 부분 수열의 최대 길이
  for j in range(0, i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i],dp[j] +1)
      
print(n - max(dp)) 