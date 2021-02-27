import sys

onezeros = input()
zero = 0
one = 0
beforeNum = onezeros[0]

if beforeNum == "0":
  one += 1
else:
  zero += 1

for i in range(0,len(onezeros)):
  if onezeros[i] != beforeNum:
    if onezeros[i] == "0":
      one += 1
    else:
      zero += 1
  beforeNum = onezeros[i]

print(min(zero, one))
