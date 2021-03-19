def solution(N, stages):
    answer = []
    temp=[] 
    total=len(stages) 
    for i in range(1,N+1):
        cnt=0
        for j in stages:
            if i==j:
                cnt=cnt+1 
        if total==0: #스테이지에 도달한 유저가 없는 경우
            fail=0
        else:
            fail=cnt/total
        temp.append((i,fail))  
        total=total-cnt
    
    temp=sorted(temp, key=lambda x: x[1], reverse=True) #내림차순
    answer=[i[0] for i in temp]
    return answer