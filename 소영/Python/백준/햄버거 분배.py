import sys

howlong, position = map(int, sys.stdin.readline().split())
inputString = sys.stdin.readline().rstrip()

result = 0
nowHam = -1

for i in range(0,len(inputString)):
  if inputString[i] == "P":
    for j in range(max(nowHam+1, i-position),min(i+position+1, howlong)):
      if inputString[j] == "H":
        result += 1
        nowHam = j
        break


print(result)
