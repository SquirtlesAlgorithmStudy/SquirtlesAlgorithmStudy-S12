# 작성자 : SH_WON_96
# 2021-03-16
# 알고리즘 - Sort
# 문제번호 : 프로그래머스 2019 KAKAO BLIND 실패율 / level 2
"""
N1,stages1 = 5,[2,1,2,6,2,5,3,3]
solution(N1,stages1) # [3,4,2,1,5]

N2,stages2 = 4,[4,4,4,4,4]
solution(N1,stages2) # [4,1,2,3]

"""
# N - 전체 스테이지 갯수
# stages - 사용자가 멈춰있는 스테이지의 번호가 담긴 배열



def solution(N, stages):

    stagesum = [0 for _ in range(N+2)] # 1~ N+1 까지 N개

    # 각 스테이지마다 실패한 사람들 늘렸음
    for i in stages:
        if i == N+2:
            continue
        else:
            stagesum[i]+= 1
    fail = []
    rm = 0
    totnum = len(stages)
    for i in range(N+1):
        if stagesum[i] == 0 and totnum == 0:
            fail.append(0)
        else:
            fail.append(stagesum[i]/totnum)
            totnum -= stagesum[i]

    # print("stagesum"+str(stagesum))
    # print(fail)
    result = []
    for i, t in enumerate(fail[1:]):
        result.append([i+1,t])
    #print(result)
    result = sorted(result,key = lambda x : -x[1])
    tmp = []
    for _ in result:
        tmp.append(_[0])

    return tmp


# N1,stages1 = 5,[2,1,2,6,2,4,3,3]
# print(solution(N1,stages1)) # [3,4,2,1,5]

# N2,stages2 = 4,[4,4,4,4,4]
# print(solution(N2,stages2)) # [4,1,2,3]

N3 = 5
stages3 = [2,1,2,4,2,4,3,3]
print(solution(N3,stages3)) # [4,1,2,3]