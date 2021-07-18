N = int(input())
score = []
answer = 0

for i in range(N):
  a = int(input())
  score.append(a)

#1
for i in range(N-1, 0, -1):
  if i == 0:
    break
  if score[i] == score[i -1]:
    answer += 1
    score[i -1] -= 1
  elif score[i] < score[i -1]:
    answer += score[i -1] - score[i] + 1
    score[i -1] -= score[i -1] - score[i] + 1

print(answer)

#2 시간초과
for i in range(N-1 , 0, -1):
  if i == 0 :
    break
  while score[i] >= score[i-1] :
    answer += 1
    score[i-1] -= 1
    

