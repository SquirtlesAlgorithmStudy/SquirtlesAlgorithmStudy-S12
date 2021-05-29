from collections import deque

def splitstring(w):
    stack = [1]
    first = w[0]
    i = 1
    while stack:
        if w[i] == first : 
            stack.append(1)
        else : stack.pop()
        i += 1
    u = w[0:i]
    v = w[i:]
    return (u, v)

def testright(w):
    if w[0] == '(' and w[len(w)-1] == ')': return True
    else : return False

def modiu(w):
    wd = deque(list(w))
    wd.popleft()
    wd.pop()
    for i in range(len(wd)):
        if wd[i] == '(' : wd[i] = ')'
        else : wd[i] = '('
    wd = ''.join(wd)
    return wd
         
    
def modifing(w):
    if w == '' : return ''
    u, v = splitstring(w)
    if(testright(u)): return u + modifing(v)
    else : return '(' + modifing(v) + ')' + modiu(u)         

def solution(p):
    if p == '' : return ''
    answer = modifing(p)
    return answer