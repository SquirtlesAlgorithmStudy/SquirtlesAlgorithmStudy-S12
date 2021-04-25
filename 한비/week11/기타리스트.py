import sys
input=sys.stdin.readline


N,S,M=map(int,input().split())
play_list = list(map(int, input().split()))
possible_volumns=[]

def solve(start, possible, M):
    nxt=set()
    if start[0]==-1 or len(start)==0:
        return -1
    for volumn in start:
        if volumn+possible<=M:
            nxt.add(volumn+ possible)
        if volumn-possible>=0:
            nxt.add(volumn- possible)
    if len(nxt)==0:
        return -1
    return list(nxt)

start = [S]
check = True
for possible in play_list:
    if start[0]==-1 or len(start)==0:
        check = False
        print(-1)
        break
    else:
        start=solve(start, possible, M)

if check:
    print(max(start))