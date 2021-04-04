# 작성자 : SH_WON_96
# 2021-04-03
# 알고리즘 - BFS
# 문제번호 : 9019 DSLR

import sys
from collections import deque
fast_in = sys.stdin.readline

N = int(fast_in().strip())

def D(number):
    return number*2%10000

def S(number):
    if number:
        return number - 1
    else:
        return 9999
def L(number):
    return int(number%1000*10 + number//1000)

def R(number):
    return int(number%10*1000+ number//10)


def calculate(x1,x2):
    q = deque()
    numbers = [False for _ in range(10000)]
    numbers[x1] = True
    q.append([x1,""])
    while q:
        y, res = q.popleft()

        if y == x2:
            print(res)
            break

        n1 = D(y)
        if not numbers[n1]:
            numbers[n1] = True
            q.append([n1,res+"D"])

        n1 = S(y)
        if not numbers[n1]:
            numbers[n1] = True
            q.append([n1, res + "S"])

        n1 = L(y)
        if not numbers[n1]:
            numbers[n1] = True
            q.append([n1, res + "L"])

        n1 = R(y)
        if not numbers[n1]:
            numbers[n1] = True
            q.append([n1, res + "R"])

for _ in range(N):
    t1, t2 = map(int,fast_in().strip().split())

    calculate(t1,t2)