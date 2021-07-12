S = input()

a = S.split('0')
b = S.split('1')

result = [i for i in a if i in [""]]
A = len(a)-len(result)

result = [i for i in b if i in [""]]
B = len(b)-len(result)

if A > B :
  print(B)
else :
  print(A)

  