#후위 표기식 2
#백준 1935

import sys

input = sys.stdin.readline

n = int(input())
peq = list(input())
operand = [int(input()) for _ in range(n)]

peq.pop()

for i in range(len(peq)):
    letter = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if peq[i] in letter: peq[i] = operand[ord(peq[i])-ord("A")]

while len(peq) != 1:
    for i in range(len(peq)):
        if peq[i] in list('+-*/'):
            peq[i] = eval(str(peq[i-2])+str(peq[i])+str(peq[i-1]))
            del peq[i - 1]
            del peq[i - 2]
            
            break

print('%.2f' %peq[0])


'''
후위 표기식 1 구현
입력 : 3+2*4-2 일 때 후위 표기식으로 출력하기
peq = []
oper = []


for i in eq:
 if i == "*" or i == "/" or i == "(":
   oper.append(i)
 elif i == "+" or i =="-":
   for _ in range(len(oper)):
     peq.append(oper.pop())
   oper.append(i)
 elif i == ")":
   while j != "(" :
     peq.append(oper.pop())
   oper.pop()
 else:
   peq.append(i)
peq.pop()
for i in range(len(oper)):
  peq.append(oper.pop())
'''