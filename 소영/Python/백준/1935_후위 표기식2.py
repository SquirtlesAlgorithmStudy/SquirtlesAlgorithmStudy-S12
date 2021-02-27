num = int(input()) # 피연산자 개수
str = input() # 후위 표기식

getnum = []
for i in range(num):
  getnum.append(int(input()))


storage = []
result = 0


for i in str:
  if 'A' <= i <= 'Z': # 문자일 때
    storage.append(getnum[ord(i)-ord('A')])
  else:
    second = storage.pop()
    first = storage.pop()

    if i == '+':
      storage.append(first+second)
    elif i == '-':
      storage.append(first-second)
    elif i == '*':
      storage.append(first*second)
    elif i == '/':
      storage.append(first/second)

print(format(storage[0],".2f"))
