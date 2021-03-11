import sys
input = sys.stdin.readline

string = input().strip()

# 올바른 괄호인지 검사
def check_string(s):
    stack = [] #스택선언
    for i in s:
        if i == '(' or i == '[': #여는 괄호 일때 스택에 넣어주기
            stack.append(i)
        elif i == ')' and stack:
            if stack[-1] == '(':
                stack = stack[:-1] #"()"완성 됐으므로 pop
            else:
                stack.append(i) #아니면 일단 넣는다
        elif i == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(i)
        else:
            stack.append(i)
    if stack: #스택에 값이 남아있으면
        return False
    else:
        return True

#올바른 괄호라면 계산
def calculate(s):
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(': #바로 top에 짝이 있을경우
                stack[-1] = 2 #스택에 2넣어주기
            else:
                tmp = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j] == '(': # 숫자 대신 "("를 만나면
                        stack[-1] = tmp * 2 #이제까지 계산한 숫자에 *2를 스택에 저장
                        break
                    else: #숫자가 나오면
                        tmp += stack[j] #숫자를 tmp에 저장
                        stack = stack[:-1] #저장한 숫자 pop
        elif i == ']':
            if stack[-1] == '[': #[]짝이 맞춰지면 스택에 3넣어주기
                stack[-1] = 3
            else:
                tmp = 0
                for k in range(len(stack)-1, -1, -1):
                    if stack[k] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[k] 
                        stack = stack[:-1]
    return sum(stack)

if check_string(string) == False:
    print(0)
else:
    print(calculate(string))