def solution(name):
    answer = 0
    answer = len(name) -1
    for i in range(len(name)):
        if name[i] == 'A':
            answer -= 1
    for i in range(len(name)):
        if name[i] == 'B'or'Z' :
            answer += 1
        elif name[i] == 'C' or 'Y':
            answer += 2
        elif name[i] == 'D' or 'X' :       
            answer += 3
        elif name[i] == 'E' or 'W' :
            answer += 4
        elif name[i] == 'F' or 'V' :
            answer += 5   
        elif name[i] == 'G' or 'U' :
            answer += 6       
        elif name[i] == 'H' or 'T' :
            answer += 7       
        elif name[i] == 'I' or 'S' :
            answer += 8       
        elif name[i] == 'J' or 'R' :
            answer += 9       
        elif name[i] == 'K' or 'Q' :
            answer += 10       
        elif name[i] == 'L' or 'P' :
            answer += 11       
        elif name[i] == 'M' or 'O' :
            answer += 12
        elif name[i] == 'N' :
            answer += 13       
    return answer
