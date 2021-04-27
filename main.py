import sys
fastin = sys.stdin.readline

n, s, m = map(int, fastin().split())
v = list(map(int, fastin().split()))
d = []
d.append(min(s + v[0], m))