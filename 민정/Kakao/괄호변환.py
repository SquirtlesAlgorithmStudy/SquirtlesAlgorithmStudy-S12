def balance(p):
    num = 0
    for idx in p:
        if idx == '(': num+=1
        else: num-=1
    return not(bool(num))

def correct(p):
    num = 0
    if balance(p) == False: return False
    for idx in p:
        if idx == '(': num+=1
        else: num-=1
        if num<0: return False
   # if balance(p).num<0: return False
    
    return True

def solution(p):
    if correct(p) == True: return p
    for i in range(2, len(p)+1, 2):
        if balance(p[:i]) == True:
            u, v = p[:i], p[i:]
            break
    if correct(u) == True:
        return (u+solution(v))
    else:
        answer = '(' + solution(v) +')'
        for i in u[1:-1]:
            if i == '(': answer += ')'
            else: answer += '('
    return answer