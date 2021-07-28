def solution(s):
    answer = 0
    answer += len(s)
    S = list(s)
    # 전체 길이에서 줄어든만큼 빼어나감
    # 2개연속까진 하나 안하나 똑같음
    # 연속된수는 문자길이의 절반이 최대
    '''
    aa = 2a
    aaa = 3a      3 > 2
    abab = 2ab    4 > 3        1  
    ababab = 3ab  6 > 3        3

    abcabc = 3abc  6 > 4       2  
    abcabcabc = 3abc 9 > 4     5 
    '''
    for i in range(len(s)):
      for j in range(len(s)//2):
        if S[i:i+j] == S[i+j:2*(i+j)] :
            answer -= (i+j)
        
    return answer