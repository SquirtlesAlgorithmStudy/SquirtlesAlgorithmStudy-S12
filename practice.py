def splitstring(w):
    stack = [1]
    first = w[0]
    i = 1
    while stack:
        if w[i] == first : 
            stack.append(1)
        else : stack.pop()
        i += 1
        print(i)
    u = w[0:i]
    v = w[i:]
    
    return (u, v)


a = splitstring("((()()))()()")
print(a)
