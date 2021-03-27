# 작성자 : SH_WON_96
# 2021-03-27
# 알고리즘 - 이진 탐색
# 문제번호 : 2110 공유기 설치

# 초기 입력값 받기
import sys
fast_in = sys.stdin.readline

N,C = map(int, fast_in().strip().split())
house = []

for _ in range(N):
    house.append(int(fast_in().strip()))

house.sort()
#print(house)
# 가장 인접한 공유기 사이의 거리를 최대 --> 모든 공유기가 적당히 다 떨어져있어야함. 제일 가까운 거리를 maximize
start = 1 # 라우터 최소길이 1 부터
end = house[-1] - house[0] #라우터 최대길이 end

# 시작하는 집과 끝에 있는 집 가운데를 기준으로...

def checkdist(dist):
    count = 1
    router = house[0] # 시작점을 기준으로 dist 만큼의 거리로 라우터를 놓는다면 총 몇개의 라우터가 필요한지를 체크함
    for i in range(1,N):
        if router + dist <= house[i]: # dist거리를 넘어서 집이 존재한다면 그 집에도 라우터 설치해줘야함
            count += 1
            router = house[i] # 그럼 이제 새로운 라우터 기준점이 바뀐거지

    return count

while start <= end:
    mid = (start+end)//2 # 중앙값을 기준 길이로 시작해서

    if checkdist(mid) >= C: # 중앙값 길이로 했을때 몇개의 라우터가 필요한지 확인해서 C보다 크면 길이가 너무 짧아서 많이 쓴거야
        # 이거 == C 랑  > C 로 나누면. 길이가 최대인경우를 탐색 못함
        result = mid
        start = mid + 1 # 그렇다면 길이를 늘이기 위해서 start를 mid + 1로 옮김
    else: # C보다 갯수가 적으면 그건 너무 길게해준거니까 짧게 해줘야함
        end = mid - 1 # 짧게하려면 중앙아래로 end를 바꿔줘야지지

print(result)
