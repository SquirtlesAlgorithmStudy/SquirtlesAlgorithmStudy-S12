# 작성자 : SH_WON_96
# 2021-02-27
# 알고리즘 - 재귀
# 문제번호 : 6603 로또

import sys
from itertools import combinations
input = sys.stdin.readline

case = []

while True:
    tmp = input().strip()
    if len(tmp) == 1:
        break
    case.append(list(map(int,tmp.split())))

result = []
for test in case:
    result = list(combinations(test[1:],6)) # tuple이 들어있는 list로 반환됨
    for i in range(len(result)):
        print(" ".join(str(_) for _ in list(result[i])))
    #print(" ".join(list(result[0])))
    print()



