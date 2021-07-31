'''
만약 길이가 1이면 답은 1
길이의 절반 이상 자르면 의미 x
1부터 절반까지 자른뒤
처음 부분을 기준으로 잡고
앞에서부터 그 다음부분이 같으면 cnt + 1
다르면 그 다음부분을 기준으로 잡아
반복

만약 cnt가 1이면
안자르는게 이득
2 이상이면
숫자길이 + 기준값

반복문 돌린뒤
min함수로 결과값 도출

'''

def solution(s):
    if len(s) == 1:
        return 1
    dap = len(s)
    for i in range(1,len(s)//2+1):
        answer = []
        mdl = s[0:i]
        mdlcnt= 1
        for j in range(i, len(s), i):
            if mdl == s[j:j+i]:
                mdlcnt += 1
            else:
                if mdlcnt == 1:
                    answer += mdl
                else:
                    answer += str(mdlcnt) + mdl
                mdl = s[j:j+i]
                mdlcnt = 1
        if mdlcnt == 1:
            answer += mdl
        else:
            answer += str(mdlcnt) + mdl
        dap = min(dap,len(answer))
    return dap
        


