#18406 럭키스트레이크

n=input()
list_n=list(n)
len_n=len(n)

# 앞 부분 숫자 합
result1=0
for i in range(int(len_n*(1/2))):
  result1=result1+int(list_n[i])

# 뒷 부분 숫자 합
result2=0
for i in range(int(len_n*(1/2))):
  result2=result2+int(list_n[int(len_n*(1/2))+i])

if (result1==result2):
  print("LUCKY")
else:
  print("READY")