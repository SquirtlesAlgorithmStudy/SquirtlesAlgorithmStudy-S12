## [1918] 후위표기식

string = list(input())
stack=[]
result=''

for s in string:
  if s.isalpha():
    result += s
  else:
    if s == '(':
      stack.append(s)
    elif s == '*' or stack[-1] == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        result += stack.pop()
      stack.append(s)
    elif s == '+' or s == '-':
      while stack and stack[-1] != '(':
        result += stack.pop()
      stack.append(s)
    elif s == ')':
      while stack and stack[-1] != '(':
        result += stack.pop()
      stack.pop()

while stack:
  result += stack.pop()
print(result)