def solution(number, k):
    result=[]
    index = 0
    for i in range(len(number)-k):
        if "9" in number[index:k+i+1]: max_val = "9" #9 와 같은 특수한 경우는 쓸데 없이 맥스함수 돌릴 필요 없게 한다.
        else: max_val = max(number[index:k+i+1])
        for j in range(index,len(number)-1):
            if number[j] == max_val:
                index = j+1
                break
        result.append(max_val)    
    
    answer = "".join(result)
    return answer

print(solution("4177252842", 4))






'''
처음 풀이를 할 때는 입력 받은 것을 싹 다 int 자료형으로 바꾼 뒤에 다시 막 10곱하기 뭐시기 이런거 써서 다 합쳐준 뒤 str로 변형했는데 위 코드 처럼 문자열 자체에서 연산해주고 join으로 합쳐주는게 훨 낫다!

def solution(number, k):
    answer = 0
    data = list(number)
    data_int = [int(i) for i in data]
    result_int=[]
    index = 0
    for i in range(len(data_int)-k):
        max_val = max(data_int[index:k+i+1])
        for j in range(index,len(data_int)-1):
            if data_int[j] == max_val:
                index = j+1
                break
        result_int.append(max_val)    
    
    for i in range(len(result_int)):
        answer += ((10 ** (len(result_int)-i-1)) * result_int[i])
    answer = str(answer)
    return answer

'''
    

        