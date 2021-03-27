# 작성자 : SH_WON_96
# 2021-03-23
# 알고리즘 - DP
# 문제번호 : 14501 퇴사

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N = int(fast_in().strip())
table = []
dp = []

for i in range(N):
    t,p = map(int,fast_in().strip().split())
    table.append([t,p])
    dp.append(p)

dp.append(0)
print(table)
print(dp)

for i in range(N-1,-1,-1): # 뒤에서부터 거슬러 올라올꺼야 내가 일끝나는 날이 N을 넘지 않도록
    t = table[i][0] # 걸리는 날짜
    p = table[i][1] # 금액
    if i + t > N: # 일을 시작하는날 + 걸리는 기간 > N 이면 일 못하니깐
        dp[i] = dp[i+1] # (i+1)일에 일했을 때 금액이랑 같아짐 // 뒤에서부터 왔고, 일을 못했으니까 같아지겠지
    else: # 일을 할 수 있으면
        dp[i] = max(dp[i+1],p+dp[i+t]) # (i+1)일에 할 수 있는 금액이랑, 내가 오늘 일하고 (i+t)일에 일 했을때 받는 금액이랑 비교해서 큰걸로

print(dp[0])