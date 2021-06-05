import heapq
def readdata(s):
    heap = []
    i = 1
    while True :
        if s[i] == '{':
            temp = []
            while True:
                
                if s[i] == '}' : 
                    heapq.heappush(heap, (len(temp), temp))
                    break
                i += 1
                j = 0
                while True:
                    if s[i] == ',':break
                    elif s[i] == '}':break
                    j += 1
                    i += 1
                temp.append(int(s[i-j:i]))
        i += 1
        if i == len(s) : return heap
            

def solution(s):
    answer = []
    temp = []
    heap = readdata(s)
    for _ in range(len(heap)):
        temp.append(set(heapq.heappop(heap)[1]))
    answer.append(list(temp[0])[0])
    for i in range(1, len(temp)):
      answer.append((list(temp[i]-temp[i-1]))[0])   
    return answer
