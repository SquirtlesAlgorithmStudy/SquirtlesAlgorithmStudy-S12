# 거스름돈
'''
n = int(input())
count = 0
coins = [500, 100, 50, 10]

for i in coins:
  count += (n // i)
  n %= i

print(count)
'''

# 큰 수의 법칙
'''
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
sum = 0 
i = 0
count= k 
data = sorted(data, reverse = True)

while m > 0:
  sum += data[i]
  if count == 0 :
    i -= 1
    count = k
  count -= 1
  if count == 0 : i += 1
  m -= 1

print(sum)
 
 # 교재 풀이

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
'''

'''
차이 분석
정답 코드는 수학적인 분석을 먼저 진행한 후 그 다음 코드를 작성하였다! 
나는 해당 과정을 반복문을 활용해서 직접 컴퓨터에게 일일이 연산 ! 
-> 수학적인 분석 후 알고리즘을 짜는 것이 시공간 복잡도를 줄이는 데 용이함 ! 

data.sort() : data 자체가 정렬되어 저장 (원본 리스트 변경) (연산 속도 빠르고, 불필요한 저장공간 막음)
a = sorted(data) : 원본 data는 그대로 유지, 정렬본이 a에 새로 추가되는 것 (연산속도 느림 but 기존 데이터가 살아있음)

'''

# 숫자 카드 게임
''''
n, m= map(int, input().split())
result = 0 
for i in range(n):
  card = list(map(int, input().split()))
  minimum = min(card)
  result =  max(minimum, result)
print(result)
'''
'''
max, min 함수에서 인자가 많아질수록 시간 복잡도가 늘어나고, data가 많아질수록 공간복잡도가 늘어나므로 
data[n] 이렇게 구현하면 효율성이 떨어지게 된다.

또 입력조건이 10000이하라는 점에서 min(10001, ...) 이런 방법도 가능하다.
'''

#1이 될 때 까지 
''''
n, k = map(int,input().split())
count = 0

while True:
  if n % k == 0 : n //= k
  else : n -=1
  count += 1
  if n == 1 : break

print(count)
'''
'''
n, k = map(int,input().split())
count = 0

while True:
  count += (n%k) + 1
  n = (n - (n%k))//k
  if n < k : break

count += (n-1)

print(count)
'''

'''
다음과 같이 수학 식을 이용하면 연산 효율을 더 줄일 수 있다

'''

#