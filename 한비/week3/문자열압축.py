def solution(s):
    k=len(s)//2 #조합만드는기준(총 문자열 길이의 반)
    length=len(s) #업데이트될 가장 짧은 문자열

    for i in range(1,k+1):#문자열 기준 마다 리스트 업데이트

        if i ==1:
            total_str=list(s)
            
        else :
            i = int(i)
            str_li=[]
            for j in range(0,k+1):
                j= int(j)
                str_li.append(s[i*j:i*(j+1)])
                total_str = list(filter(None, str_li))

        count=1 #같은 문자 개수 세는 변수
        encoding=""  # 압축된 문자열
        vs_str=total_str[0] # 비교대상 문자열
        
        for i in range(1,len(total_str)):

            if vs_str == total_str[i]:
                count=count+1
            else:
                if count == 1 :
                    encoding=encoding+vs_str
                    vs_str = total_str[i]
                else:
                    encoding=encoding+str(count)+vs_str
                    count = 1
                    vs_str = total_str[i]
            if i == len(total_str)-1:
                if count == 1:
                    encoding=encoding+total_str[i]
                else:
                    encoding=encoding+str(count)+vs_str
        if len(encoding) < length:
            length=len(encoding)
    answer=length
        
    return answer