def solution(name):
    answer = 0
    i = 1
    j = 1
    k = 1
    l = 1
    data = list(name)
    if len(data) == 1: return(change(data[0]))
    if len(data) == 2: return(change(data[0])+change(data[1])+1)

    if data[1] == "A":
        while True:
            if (i == (len(data)-1)) or (data[i+1] != "A") : break
            i+=1
        answer += len(data)-i-1    
    else : 
        while True:
            if(data[len(data)-j] != "A") or (j == (len(data))) : break
            j+=1
        answer += len(data)-j
        while True:
            if(data[len(data)-k] == "A") or (k == (len(data))) : break
            k+=1
        while True:
            if  (l == (len(data)-1)) or (data[l+1] == "A"):break
            l+=1
        answer = min(answer, k+l)

    for i in range(len(data)):
        answer += change(data[i])

    return answer

def change(data):
    if ord(data) <= 78: result = ord(data) - 65
    else : result = 91 - ord(data)
    return result