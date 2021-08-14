import sys
fastin = sys.stdin.readline

data = fastin().strip()

operator = []
answer =[]



for i in data:
  if i in '+-':
    for _ in range(len(operator)):
      if operator[-1] == '(': break
      answer.append(operator.pop())
    operator.append(i)
  elif i in '*/':
    if len(operator) !=0 and operator[-1] in '*/':
      for _ in range(len(operator)):
        if operator[-1] in '(+-': break
        answer.append(operator.pop())
      operator.append(i)
    else: operator.append(i)
  elif i== ')':
    for _ in range(len(operator)):
      if operator[-1] == '(':
        operator.pop()
        break
      answer.append(operator.pop())
  elif i == '(':
    operator.append(i)

  else : answer.append(i)

for _ in range(len(operator)):
  answer.append(operator.pop())

print(''.join(answer))




  
