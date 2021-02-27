# -*- coding: utf-8 -*-
import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()
dq.extend(list(sys.stdin.readline().rstrip()))
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))

new = []
res = 0
while dq:
    x = dq.popleft() #덱에서 하나씩 가져오기
    if x == '+' or x == '-' or x == '*' or x == '/':
        a = new.pop() 
        b = new.pop()

        if str(a).isalpha():
            a = num[ord(a)-ord('A')]
        if str(b).isalpha():
            b = num[ord(b)-ord('A')]

        if x == '+':
            res = b + a
        elif x == '-':
            res = b - a
        elif x == '*':
            res = b * a
        else:
            res = b / a

        new.append(res)

    else:
        new.append(x)

print(format(res,".2f"))
