import sys
fastin = sys.stdin.readline

n,c = map(int, fastin().strip().split())
home = [int(fastin().strip()) for _ in range(n)]

print(n, c, home)