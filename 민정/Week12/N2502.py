D, K = map(int, input().split())

a_pre = 0
a_cur = 1
b_pre = 1
b_cur = 1
i = 3

while i != D:
  a_pre, a_cur = a_cur, a_pre+a_cur
  b_pre, b_cur = b_cur, b_pre+b_cur
  i += 1

i=1
state = False
while True:
  j = 1
  while True:
    check = a_cur * i + b_cur * j
    if check > K: break
    elif check == K:
      state = True
      break
    j += 1
  if state: break
  i += 1
print(i)
print(j)