# 작성자 : SH_WON_96
# 2021-02-27
# 알고리즘 - 재귀
# 문제번호 : 하노이 탑 이동 순서

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 한번에 한개의 원판을 이동
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.

N = int(input().strip())

text = []
count = 0

# 시작기둥(fr) 에서 도착기둥(to) 로가는데 보조기둥(by)을 사용함
def hanoi(n, fr, by, to):
    if n == 1:
        # 원반이 1개일때는 fr 에서 to 로 가면 됨
        text.append([fr,to])
        return 1
        #return text
    else:
        # 1이 아닐 때, 가장 큰 원반을 제외한 나머지는  다 보조에 넣는다
        hanoi(n-1,fr,to,by) # n-1 을 보조로 넣는 거임
        text.append([fr,to])

        #count += 1
        # 이제 시작기둥은 비어있고, 가장 큰 원반은 도착기둥에 도착했고, 보조기둥에 순서대로 쌓인걸 다시 도착기둥에 옮겨야함.
        # "보조기둥에서 도착기둥으로, 시작기둥을 사용하여" 이니깐
        hanoi(n-1,by,fr,to)

hanoi(N,1,2,3)

print(len(text))
for move in text:
    print(move[0],move[1])