# 작성자 : SH_WON_96
# 2021-04-03
# 알고리즘 - DP
# 문제번호 : 9251 LCS


# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

t1 = " "+fast_in().strip()
t2 = " "+fast_in().strip()
LCS = [[0]*len(t2) for _ in range(len(t1))]

for i in range(1,len(t1)):
    for j in range(1,len(t2)):
        if t1[i] == t2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])


print(LCS[len(t1)-1][len(t2)-1])

