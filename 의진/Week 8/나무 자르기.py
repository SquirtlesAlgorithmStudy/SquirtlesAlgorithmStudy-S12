import sys
fastin = sys.stdin.readline

n,m = map(int,fastin().strip().split())
tree = list(map(int,fastin().strip().split()))

start = 0
end = max(tree)
result = 0
while(start <= end):
  total = 0
  mid = (start+end)//2
  total =sum([i-mid if i > mid else 0 for i in tree])
  if total < m:
    end = mid-1
  else : 
    result = mid
    start = mid + 1
print(result)