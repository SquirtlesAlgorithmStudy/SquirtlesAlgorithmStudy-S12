# 작성자 : SH_WON_96
# 2021-02-26
# 알고리즘 - 자료구조, 스택
# 문제번호 : 후위 표기식2

import sys
input = sys.stdin.readline


N = int(input().strip())

Cal = list(input().strip())
nums = []
for i in range(N):
    nums.append(int(input().strip()))

for i in range(len(Cal)):
    if Cal[i].isalpha():
        Cal[i] = nums[ord(Cal[i]) - ord("A")]

print(Cal)

def Calculate(n1,operator,n2):
    # ord("A")-ord("A") 에 위치한 nums을 가져와서 연산하면 된다.
    if operator == "+":
        return n1 + n2
    elif operator == "-":
        return n1 - n2
    elif operator == "*":
        return n1 * n2
    else:
        return n1 / n2

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

i = 0
while len(Cal) != 1:
    if isNumber(Cal[i]) == False: # float를 탐지 못함
        front = Cal[:i-2]
        result = Calculate(Cal[i-2], Cal[i],Cal[i-1])
        if i == len(Cal)-1 :
            Cal = front + [result]
            break
        back = Cal[i+1:]
        Cal = front + [result]+ back
        i = 0
    else:
        i += 1

print("%.2f"%Cal[0])


""" 
난 단계별로 다 했는데 이건 깔끔함

n=int(input())
str=input()
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
stack=[]

for s in str:
    if s.isupper():
        stack.append(nums[ord(s)-ord('A')])

    else:
        a2=stack.pop()
        a1=stack.pop()
        if s == "+":
            stack.append(a1+a2)
        elif s == "-":
            stack.append(a1-a2)
        elif s == "*":
            stack.append(a1*a2)
        elif s == "/":
            stack.append(a1/a2)

print(f"{stack[0]:.2f}")


"""




