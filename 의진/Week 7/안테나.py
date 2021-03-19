import sys
input = sys.stdin.readline
n = int(input())
pos = [i for i in map(int,input().strip().split())]
pos.sort()
index = (len(pos)-1)//2
print(pos[index])