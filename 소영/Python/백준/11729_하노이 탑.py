num = int(input())
result = []


def solution(n, start, middle, end):
  if n == 1:
    result.append((start,end))
  else :
    solution(n-1, start, end, middle);
    result.append((start, end))
    solution(n-1, middle, start, end)


solution(num,1,2,3)

print(len(result))
for i in result:
  print(*i)
