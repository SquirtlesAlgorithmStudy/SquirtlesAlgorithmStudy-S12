def solution(s):
    answer = 0
    S = list(s)
    answer += len(s)
    # 2개연속까진 하나 안하나 똑같음
    # 연속된수는 문자길이의 절반이 최대
    for i in range(len(s)-2):
        if S[i] == S[i+1] == S[i+2] :
            answer -= 1
        if S[2*i:2*i+2]==S[2*i+2:2*i+4] :
            answer -= 2
    return answer