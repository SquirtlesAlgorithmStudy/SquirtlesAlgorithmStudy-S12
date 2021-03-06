# 작성자 : SH_WON_96
# 2021-03-03
# 알고리즘 - 스택
# 문제번호 : 2504 괄호의 값

import sys
fast_in = sys.stdin.readline

text = fast_in().strip()

stack = []

for i in text:
    # 숫자나 왼쪽 괄호는 무조건 stack에 넣고 아닌 경우 체크

    # 오른쪽 ) 인 경우 괄호 안에 숫자가 있는지, 확인
    if i == ")":
        temp = 0 #괄호사이의 숫자 합
        while stack:
            top = stack.pop()
            if top == "(":
                if temp == 0: # 괄호 사이에 숫자가 없으면 그건 ()
                    stack.append(2)
                else: # 괄호사이에 숫자가 있다면 그 괄호의 2배를 stack에 넣어준다.
                    stack.append(2 * temp)
                break
            elif top == "[": # 괄호가 안맞으니 탈출
                print("0")
                exit(0)
            else: # 숫자가 등장한다면
                if temp == 0: # 첫번째 숫자이면
                    temp = int(top) # 그 숫자 넣어주기
                else: # 숫자가 이미 있었으면 숫자 더해주기
                    temp = temp + int(top)

    # 똑같은데 3으로 바꾸거나 3배 해주거나!
    elif i == "]":
        temp = 0

        while stack:
            top = stack.pop()
            if top == "[":
                if temp == 0:
                    stack.append(3)
                else:
                    stack.append(3 * temp)
                break
            elif top == "(":
                print("0")
                exit(0)
            else:
                if temp == 0:
                    temp = int(top)
                else:
                    temp = temp + int(top)

    else:
        stack.append(i)

result = 0

for i in stack:
    if i == "(" or i == "[":
        print(0)
        exit(0)
    else:
        result += i

print(result)


#print(stack[0])

"""
((()([([])]))[()])

[](()[()]()[()])()(()[()]()[()]) # 69

[()[()[()]]] # 78
[2[2[2]]]
[2[26]]
"""
