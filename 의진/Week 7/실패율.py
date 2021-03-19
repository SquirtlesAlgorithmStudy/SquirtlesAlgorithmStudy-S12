def solution(N, stages):
  cnt = [0] * (N+1)
  for i in range(len(stages)):
    cnt[stages[i]-1] += 1
  
  sum = 0
  sums = [0] * (N+1)
  res = []
  for i in range(N,-1, -1):
    sum += cnt[i]
    sums[i] = sum
  for i in range(N):
    if sums[i] == 0: res.append((i,0))
    else : res.append((i, cnt[i]/sums[i]))
  res.sort(key = lambda k:(-k[1]))
  answer = []
  for i in range(len(res)):
    answer.append(res[i][0]+1)
  return answer

N = 4
stages = [4,4,4,4,4]
print(solution(N,stages))



 