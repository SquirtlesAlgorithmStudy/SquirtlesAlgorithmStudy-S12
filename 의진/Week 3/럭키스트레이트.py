n = input()
data = [int(i) for i in n]
div = len(n) // 2 

sum_h= 0
sum_t = 0

for i in range(len(n)):
  if div >  i: sum_h += data[i]
  sum_t += data[i]

if sum_h == (sum_t - sum_h):
  print("LUCKY")
else : print("READY")



