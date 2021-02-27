from itertools import combinations # 조합

while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0: # 끝이야 ~
        break
    del inputs[0] # 0이 아니면 combinations 돌꺼니까 가장 앞에 숫자는 지워준다 !
    inputs = list(combinations(inputs, 6)) #recursion
    for i in inputs:
        for k in i:
            print(k, end=' ') # 줄바꿈 xxx & 한 칸 띄어줌
        print()
    print()
