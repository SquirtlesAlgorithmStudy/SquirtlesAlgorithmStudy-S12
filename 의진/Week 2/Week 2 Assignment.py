# 햄버거 문제

import sys

n, k = map(int, input().split())
data = list(sys.stdin.readline().rstrip())
result = 0

for i in range(n-1):
  if data[i] != 'E':
    if i >= (n-k) : k = (n-i-1)
    for j in range (k):
      if (data[i+j+1] != 'E' and data[i+j+1] != data[i]):
        result += 1
        data[i] = 'E'
        data[i+j+1] = 'E'

        break

print(result)



#반복문 내부 외부 변수의 활용

i = 0 
for i in range (5):
  print(i)
  i+=2
  print(i)

print(i)

#이를 이용한 풀이

N,K = input().split()
N = int(N)
K = int(K)
S = list(input())
j=0
result = 0
for i in range(N):
	if(S[i] != 'H'):
		for j in range(max(j,i-K),min(N,i+K+1)):
			if(S[j] != 'P'):
				result = result + 1
				j = j + 1
				break
print(result)


#동준이

n = int(input())
data=[]
for _ in range(n):
  data.append(int(input()))
result = 0

for j in range(n-1,0,-1):
  if(data[j] <= data[j-1]): 
    result += (data[j-1] - data[j]+1)
    data[j-1] -= (data[j-1] - data[j]+1)

print(result)  

'''
K = [int(input()) for _ in range(N)]
입력이 개행 형태로 주어진 경우에 list Comprehension을 이용해서 입력을 표현할 수 있다!
'''

# 예시 입출력 이외의 예의 경우도 확인할 것 !


# 항승이

n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
result = 0
cnt = 1

i = 0
while True:
  if i > n-1: break
  for j in range(l-1):
    if data[i] + j + 1 in data:
      cnt += 1
  i += cnt
  cnt = 1
  result += 1
  
print(result)
'''
# 뒤집기
'''
import sys
data = list(sys.stdin.readline().rstrip())
data = list(map(int,data))
cnt = 0

for i in range(len(data)-1):
  if data[i] != data[i+1] : cnt += 1

result = (cnt // 2) + (cnt % 2)
print(result)

#개선 풀이

data = list(map(str,input()))
cnt = 0
for i in range(len(data)-1):
  if data[i] != data[i+1] : cnt += 1
result = (cnt // 2) + (cnt % 2)
print(result)

#입력 방식에 변화를 주어서 계산 속도 개선




   





      



